import threading
import datetime
import requests as req
trd_list = ("https://images.unsplash.com/photo-1558769132-92e717d613cd?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&h=500&q=60",
            "https://img1.akspic.ru/previews/9/9/1/9/6/169199/169199-smartfon-Vozdushnyy_sharik-sinij-chelovek-zhest-500x.jpg",
            "https://img2.akspic.ru/previews/9/0/9/8/6/168909/168909-ballonchik-graffiti-ulichnoe_iskusstvo-svet-purpur-500x.jpg",
            "https://telecomdom.com/wp-content/uploads/2020/02/kartinki-na-telefon-5-576x1024.jpg",
            "https://i.pinimg.com/564x/55/36/c8/5536c8edc514d16064a65f3e20d8e181.jpg",
            "https://img3.akspic.ru/previews/7/4/2/8/6/168247/168247-kosti_3d-igra_v_kosti_3d-azartnaya_igra-pitevaya_igra-kazino-500x.jpg",
            "https://s00.yaplakal.com/pics/pics_original/2/7/5/17247572.jpg",
            "https://bipbap.ru/wp-content/uploads/2017/06/4-5.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNNucRKn044wOGq4vv4_xDngt3hH2RvvpPHw&usqp=CAU",
            "https://android-obzor.com/wp-content/uploads/2022/03/2-3.jpg")


def function_1(listok: list):
    for i in listok:
        print (i)
    with open('test_image.json', 'wb') as photo:
        photo.write(req.get(i).content)
if __name__ == '__main__':
    starting_time = datetime.datetime.today()

    thread_list = []
    for i in range(1):
        x = threading.Thread(target=function_1, args=(trd_list,), daemon=True,)
        thread_list.append(x)
        x.start()

    for thread in thread_list:
        thread.join()
    b = (datetime.datetime.today() - starting_time).seconds
    micro = (datetime.datetime.today() - starting_time).microseconds

    print(f"{b} seconds {micro} microseconds")

