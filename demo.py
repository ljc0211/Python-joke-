array = ["gkd", "ahhhhh!", "www"]

print(array)

array.append("wocao")
array.append("wocao")
array.append("wocao")

array.remove("wocao")

array.extend(["产业", "孙利龙","利龙大神真TM太帅了啊"])

def print_each(the_list):
    for each_item in the_list:
        if(isinstance(each_item, list)):
            print_each(each_item)
        else:
            print(each_item)

print_each(array)