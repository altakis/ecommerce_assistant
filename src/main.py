def main():
    print("test")
    
    from assistant_creation_scripts import packaged_tools
    
    data = packaged_tools[0]('Tea')
    
    print(data)


if __name__ == "__main__":
    main()
