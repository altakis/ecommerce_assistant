def main():
    print("test")
    
    from assistant_creation_scripts import packaged_tools, packaged_tools_funcs
    
    data = packaged_tools_funcs[1](404)
    
    print(data)


if __name__ == "__main__":
    main()
