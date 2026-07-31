import streamlit as st

st.set_page_config(page_title="Rescue Guide", page_icon="🚑", layout="wide")

FIRST_AID = {
    "Burns": [
        "Move away from the heat source.",
        "Cool the burn under cool running water for 10–20 minutes.",
        "Do not apply ice, toothpaste, or oil.",
        "Cover with a clean, non-stick cloth.",
        "Seek medical help for severe burns."
    ],
    "Bleeding": [
        "Apply direct pressure with a clean cloth or bandage.",
        "Raise the injured area if possible.",
        "Do not remove embedded objects.",
        "If bleeding does not stop, call emergency services."
    ],
    "Fainting": [
        "Lay the person flat on their back.",
        "Raise their legs slightly.",
        "Loosen tight clothing.",
        "Check breathing and responsiveness.",
        "Get medical help if they do not recover quickly."
    ],
    "Choking": [
        "Ask if they can cough or speak.",
        "If severe choking, give back blows and abdominal thrusts.",
        "Call emergency services immediately if the object does not come out."
    ],
    "Fracture": [
        "Keep the injured part still.",
        "Do not try to realign the bone.",
        "Apply a cold pack wrapped in cloth.",
        "Seek urgent medical care."
    ],
}

st.title("🚑 Rescue Guide")
st.write("A simple first-aid assistant website built with Python and Streamlit.")

col1, col2 = st.columns([1, 2])

with col1:
    category = st.selectbox("Select an emergency", list(FIRST_AID.keys()))
    show = st.button("Show first-aid steps")

with col2:
    st.subheader("First-aid instructions")
    if show:
        st.success(f"Steps for: {category}")
        for i, step in enumerate(FIRST_AID[category], 1):
            st.write(f"{i}. {step}")
    else:
        st.info("Choose an emergency and click the button to see guidance.")

st.markdown("---")
st.warning("This app is for basic guidance only. In serious emergencies, call local emergency services immediately.")
st.caption("If the person is unconscious, not breathing, or bleeding heavily, get emergency help right away.")
