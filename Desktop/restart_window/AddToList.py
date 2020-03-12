from configparser import ConfigParser


class Save :

    def onAdd(self, url, title, price):
        print(url, title , price)
        config = ConfigParser()
        print(config.read('WishList.ini'))
        # config.add_section('wishlist')
        print(config.set('wishlist', 'url', url))
        config.set('wishlist', 'title', title)
        config.set('wishlist', 'price', price)
        with open('WishList.ini', 'w') as configfile:
            config.write(configfile)
        cf = ConfigParser()
        cf.read('WishList.ini')
        print(cf.get('wishlist','price'))
        # configf.close()
        print(cf.sections())
        configfile.close()
