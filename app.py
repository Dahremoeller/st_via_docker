import streamlit as st
import os


def save_uploaded_file(uploaded_file):
    # Create the directory if it doesn't exist
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    # Define the path to save the file
    save_path = os.path.join("tmp", uploaded_file.name)

    # Write the file's contents to the new path in binary mode
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    return st.success(f"File {uploaded_file.name} saved successfully to temp_files!")


st.title("My dashboard")

file = st.file_uploader(
    "Your file",
    type=None,
    accept_multiple_files=False,
    key=None,
    help=None,
    on_change=None,
    args=None,
    kwargs=None,
)

if file is not None:
    # Get details about the uploaded file
    file_details = {"FileName": file.name, "FileType": file.type}
    st.write(file_details)

    # Save the uploaded file
    save_uploaded_file(file)
