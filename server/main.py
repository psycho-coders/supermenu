from web import app


# TODO: use config
if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0')
    except Exception as e:
        print(f"FATAL, msg: {e}")
