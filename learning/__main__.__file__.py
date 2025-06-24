if __name__ == "__main__":
    import __main__
    import pathlib

    main_file = __main__.__file__
    print(f"Main file: '{main_file}' is of type «{type(main_file)}»")
    main_folder = pathlib.Path(main_file).resolve().parent

    print(f"Main folder: '{main_folder}' is of type «{type(main_folder)}»")

    for _item in dir(__main__):
        print(f"{_item}")
