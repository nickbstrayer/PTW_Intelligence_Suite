import streamlit as st

# Simulated user database
user_db = {
    "admin": "password123",
    "user@example.com": "welcome123"
}

def initialize_session_state():
    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False
    if "login_email" not in st.session_state:
        st.session_state.login_email = ""
    if "user_role" not in st.session_state:
        st.session_state.user_role = "member"
    if "page" not in st.session_state:
        st.session_state.page = "landing"

def render_auth_page():
    mode = st.query_params.get("mode", "login")

    st.markdown("### 🔐 PTW Intelligence Suite")

    # Auth form
    auth_mode = st.radio("Choose Option", ["Login", "Register"], index=0 if mode == "login" else 1)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if auth_mode == "Login":
        if st.button("Login"):
            if email in user_db and user_db[email] == password:
                st.session_state.is_authenticated = True
                st.session_state.login_email = email
                st.session_state.user_role = "admin" if email == "admin" else "member"
                st.success("Login successful!")
                st.rerun()  # <-- updated here
            else:
                st.error("Invalid email or password.")
    else:
        if st.button("Register"):
            if email in user_db:
                st.warning("Email already registered.")
            else:
                user_db[email] = password
                st.success("Registration successful. Please log in.")
