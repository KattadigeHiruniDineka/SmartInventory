
import streamlit as st
import pandas as pd

from product import Electronics, Grocery
from inventory import Inventory


# -----------------------------------
# PAGE SETTINGS
# -----------------------------------
st.set_page_config(
    page_title="StockSmart",
    page_icon="📦",
    layout="wide"
)


# -----------------------------------
# GREEN AND WHITE DESIGN
# -----------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #F3F8F4;
    color: #1B3324;
}

h1, h2, h3, h4 {
    color: #14532D !important;
}

.stApp p,
.stApp label {
    color: #263B2D;
}

/* Input boxes */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #172B1D !important;
    border: 1px solid #86B99A !important;
    border-radius: 8px !important;
}

/* Input placeholder */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #66756A !important;
    opacity: 1;
}

/* Dropdown */
[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #172B1D !important;
    border-color: #86B99A !important;
}

[data-baseweb="select"] * {
    color: #172B1D;
}

/* Dashboard cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #C7E2CF;
    box-shadow: 0 3px 8px rgba(20, 83, 45, 0.08);
}

[data-testid="stMetricLabel"] {
    color: #365743 !important;
}

[data-testid="stMetricValue"] {
    color: #15803D !important;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background-color: #15803D !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

.stButton > button p,
.stFormSubmitButton > button p {
    color: #FFFFFF !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #166534 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    color: #365743 !important;
}

.stTabs [aria-selected="true"] {
    color: #15803D !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #E5F1E8;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------------
# INVENTORY INITIALIZATION
# -----------------------------------
if "inventory" not in st.session_state:
    inventory = Inventory()

    inventory.add_product(
        Electronics(
            "P001",
            "Wireless Keyboard",
            3500,
            10
        )
    )

    inventory.add_product(
        Electronics(
            "P002",
            "Computer Mouse",
            1800,
            4
        )
    )

    inventory.add_product(
        Grocery(
            "P003",
            "Milk Powder",
            1200,
            20
        )
    )

    st.session_state.inventory = inventory

inventory = st.session_state.inventory


# -----------------------------------
# SUCCESS / ERROR MESSAGE HANDLING
# -----------------------------------
if "flash_message" in st.session_state:
    message_type, message_text = st.session_state.flash_message

    if message_type == "success":
        st.success(message_text)
    elif message_type == "error":
        st.error(message_text)

    del st.session_state.flash_message


# -----------------------------------
# HEADER
# -----------------------------------
st.title("📦 StockSmart")
st.caption("Smart Inventory Management System")
st.markdown("---")


# -----------------------------------
# DASHBOARD SUMMARY
# -----------------------------------
total_products = len(inventory.products)

total_quantity = sum(
    product.quantity for product in inventory.products
)

total_value = inventory.total_stock_value()

low_stock_count = len(
    inventory.low_stock_products()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Products", total_products)
col2.metric("Units in Stock", total_quantity)
col3.metric("Stock Value", f"Rs. {total_value:,.2f}")
col4.metric("Low Stock Alerts", low_stock_count)


if low_stock_count > 0:
    st.warning(
        f"⚠️ {low_stock_count} product(s) have "
        "5 or fewer units in stock."
    )
else:
    st.success("✅ All products have sufficient stock.")


# -----------------------------------
# NAVIGATION TABS
# -----------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Products",
    "➕ Add Product",
    "🛒 Sales",
    "📦 Restock"
])


# -----------------------------------
# TAB 1: PRODUCTS
# -----------------------------------
with tab1:
    st.subheader("Product Inventory")

    if inventory.products:
        search = st.text_input(
            "🔍 Search by product name or ID",
            key="product_search",
            placeholder="Enter product name or ID..."
        ).strip().lower()

        filtered_products = [
            product
            for product in inventory.products
            if search in product.name.lower()
            or search in product.product_id.lower()
        ]

        if filtered_products:
            rows = []

            for product in filtered_products:
                if product.quantity <= 5:
                    status = "⚠️ Low Stock"
                else:
                    status = "✅ In Stock"

                rows.append({
                    "Product ID": product.product_id,
                    "Product Name": product.name,
                    "Category": product.category,
                    "Price (Rs.)": product.price,
                    "Quantity": product.quantity,
                    "Stock Value (Rs.)": product.stock_value(),
                    "Status": status
                })

            st.dataframe(
                pd.DataFrame(rows),
                width="stretch",
                hide_index=True
            )
        else:
            st.info("No matching products found.")
    else:
        st.info("No products available. Please add a product.")


# -----------------------------------
# TAB 2: ADD PRODUCT
# -----------------------------------
with tab2:
    st.subheader("➕ Add a New Product")

    with st.form("add_product_form", clear_on_submit=True):
        product_id = st.text_input(
            "Product ID",
            placeholder="Example: P004"
        )

        name = st.text_input(
            "Product Name",
            placeholder="Enter product name"
        )

        category = st.selectbox(
            "Category",
            ["Electronics", "Grocery"]
        )

        price = st.number_input(
            "Price (Rs.)",
            min_value=0.01,
            value=100.0,
            step=50.0
        )

        quantity = st.number_input(
            "Initial Quantity",
            min_value=0,
            value=1,
            step=1
        )

        add_submitted = st.form_submit_button("➕ Add Product")

    if add_submitted:
        try:
            if not product_id.strip() or not name.strip():
                raise ValueError(
                    "Please enter both Product ID and Product Name."
                )

            if category == "Electronics":
                new_product = Electronics(
                    product_id.strip(),
                    name.strip(),
                    price,
                    quantity
                )
            else:
                new_product = Grocery(
                    product_id.strip(),
                    name.strip(),
                    price,
                    quantity
                )

            inventory.add_product(new_product)

            st.session_state.flash_message = (
                "success",
                f"✅ {name.strip()} added successfully!"
            )

            st.rerun()

        except ValueError as error:
            st.error(f"❌ Could not add product: {error}")


# -----------------------------------
# TAB 3: SALES
# -----------------------------------
with tab3:
    st.subheader("🛒 Sell a Product")

    if inventory.products:
        with st.form("sell_form", clear_on_submit=True):
            selected_id = st.selectbox(
                "Select Product",
                [product.product_id for product in inventory.products],
                format_func=lambda product_id: (
                    f"{product_id} - "
                    f"{inventory.find_product(product_id).name} "
                    f"(Stock: "
                    f"{inventory.find_product(product_id).quantity})"
                )
            )

            sell_amount = st.number_input(
                "Quantity to Sell",
                min_value=1,
                value=1,
                step=1
            )

            sell_submitted = st.form_submit_button("🛒 Complete Sale")

        if sell_submitted:
            try:
                product = inventory.find_product(selected_id)
                product_name = product.name

                inventory.sell_product(selected_id, sell_amount)

                st.session_state.flash_message = (
                    "success",
                    f"✅ Sale successful! {sell_amount} unit(s) "
                    f"of {product_name} sold."
                )

                st.rerun()

            except ValueError as error:
                st.error(f"❌ Sale failed: {error}")

    else:
        st.info("Please add a product before making a sale.")


# -----------------------------------
# TAB 4: RESTOCK
# -----------------------------------
with tab4:
    st.subheader("📦 Restock Products")

    if inventory.products:
        with st.form("restock_form", clear_on_submit=True):
            restock_id = st.selectbox(
                "Select Product to Restock",
                [product.product_id for product in inventory.products],
                format_func=lambda product_id: (
                    f"{product_id} - "
                    f"{inventory.find_product(product_id).name} "
                    f"(Stock: "
                    f"{inventory.find_product(product_id).quantity})"
                )
            )

            restock_amount = st.number_input(
                "Quantity to Add",
                min_value=1,
                value=1,
                step=1
            )

            restock_submitted = st.form_submit_button("📦 Update Stock")

        if restock_submitted:
            try:
                product = inventory.find_product(restock_id)
                product_name = product.name

                inventory.restock_product(
                    restock_id,
                    restock_amount
                )

                st.session_state.flash_message = (
                    "success",
                    f"✅ Restock successful! {restock_amount} unit(s) "
                    f"added to {product_name}."
                )

                st.rerun()

            except ValueError as error:
                st.error(f"❌ Restock failed: {error}")

    else:
        st.info("Please add a product before restocking.")


# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")
st.caption("StockSmart | Python OOP Project")
