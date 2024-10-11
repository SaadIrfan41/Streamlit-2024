import streamlit as st

# # Title
st.title("Streamlit Text Display Example")

# # Header
st.header("This is a Header")

# # Subheader
st.subheader("This is a Subheader")

# # Text (Used to Emphasize some text)
st.text("This is a simple text")

# # Write (Default font of your browser)
st.write("This is written using st.write()")

# Markdown
st.markdown("# This is a Markdown heading")
st.markdown("[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)")
st.markdown("This is a Markdown paragraph with **bold** and *italic* text")
st.markdown("""
        1. step 1
        2. step 2

        - unordered step 1
        - step 2
            - substep 2.1
""")

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language="python")

# Emojis
st.markdown("### Emojis")
st.markdown("[Emojis](https://share.streamlit.io/streamlit/emoji-shortcodes)")
st.markdown("Here are some emojis:")
st.markdown(":thumbsup: :heart: :rocket: :smile:")

# HTML
st.header("HTML")
st.html("""
         <h1 style='color: blue;'>This is a blue heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
 """)

# Divider
st.markdown("""---""")
st.divider()

# LaTeX
st.latex(r"e^{i\pi} + 1 = 0")
st.latex(r"f(x) = x^2 + 2x + 1")
st.latex(r"g(x) = \frac{1}{x}")
st.latex(r"h(x) = \sqrt{x}")
st.latex(r"y = mx + c")
st.latex(r"a^2 + b^2 = c^2")
