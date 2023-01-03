from web import app


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"FATAL, msg: {e}")
