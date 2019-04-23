#add wallet and wishlist variables


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            auction = Listing(artwork, price, self)
            veneer.add_listing(auction)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    artwork.owner = self
                    veneer.remove_listing(listing)


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, remove_item):
        self.listings.remove(remove_item)

    def show_listings(self):
        for item in self.listings:
            print(item)


class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{artist}. \"{name}\". {year}, {medium}. {owner_name}, {owner_location}".format(artist=self.artist,
                                                                                               name=self.title,
                                                                                               year=self.year,
                                                                                               medium=self.medium,
                                                                                               owner_name=self.owner.name,
                                                                                               owner_location=self.owner.location)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "%s, $%s." % (self.art, self.price)


veneer = Marketplace()
edytta = Client("Edytta Halpirt", 'Private Collection', False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Telier)", "oil on canvas", 1910, edytta)

edytta.sell_artwork(girl_with_mandolin, "6M (USD)")
moma.buy_artwork(girl_with_mandolin)
print(veneer.show_listings())
print(girl_with_mandolin)