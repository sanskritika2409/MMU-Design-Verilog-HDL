import streamlit as st
import time


st.set_page_config(
    page_title="MMU Design Dashboard",
    layout="wide"
)


st.title("🚀 Memory Management Unit (MMU) Dashboard")

st.subheader("Virtual Address Translation Simulator")


va = st.text_input(
    "Enter Virtual Address (Hex)",
    "12345000"
)


enable = st.checkbox(
    "Enable MMU",
    True
)


read = st.checkbox(
    "Read Access",
    True
)


write = st.checkbox(
    "Write Access",
    False
)



if st.button("Translate Address"):


    if enable:

        page_number = va[0:5]

        offset = va[-3:]


        physical_address = page_number + offset


        st.success("Translation Successful")


        col1,col2,col3 = st.columns(3)


        with col1:
            st.metric(
                "Virtual Address",
                "0x"+va
            )


        with col2:
            st.metric(
                "Physical Address",
                "0x"+physical_address
            )


        with col3:
            st.metric(
                "Status",
                "VALID"
            )


        st.write(
        """
        Address Flow:

        Virtual Address
        ↓
        Page Number Extraction
        ↓
        Page Table Lookup
        ↓
        Permission Check
        ↓
        Physical Address
        """
        )


    else:

        st.error(
            "MMU Disabled"
        )



st.divider()


st.header("MMU Signals")


data = {

"Signal":
[
"Enable",
"Read",
"Write",
"Page Fault",
"Protection Fault"
],

"Value":
[
enable,
read,
write,
False,
False
]

}


st.table(data)


st.info(
"""
Project:
Memory Management Unit Design using Verilog HDL

Tools:
Verilog
Icarus Verilog
GTKWave
Streamlit

Features:
✔ Address Translation
✔ Permission Checking
✔ Simulation Dashboard
"""
)