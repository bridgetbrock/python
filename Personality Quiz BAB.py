import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

show = pg.prompt ("What is your favorite show? ") .lower()
if show == "thomas the train":
    pg.alert ("You have great taste! ")
    points += 65
    wb.open ("https://www.youtube.com/watch?v=GnrwM7vFn_U")
elif show == "wicked tuna":
    pg.alert ("I hate fishing!")
    points -= 54
    wb.open ("https://www.youtube.com/watch?v=zJfxdVI1Jio")
elif show == "hannah montana":
    pg.alert ("I love that show")
    points += 87
    wb.open ("https://www.youtube.com/watch?v=nDMIuuO_PQo")
elif show == "backyardigans":
    pg.alert ("I used to watch that show!")
    points += 26
    wb.open ("https://www.youtube.com/watch?v=sk6kBjStCf0")
elif show == " backyardigans":
    pg.alert ("I used to watch that show!")
    points += 35
    wb.open ("https://www.youtube.com/watch?v=sk6kBjStCf0")
elif show == "andi mack":
    pg.alert ("I used to watch that!")
    points += 829
    wb.open ("https://www.youtube.com/watch?v=8uWcx8YGAzM")
else:
    pg.alert ("Your favorite show is " + show)
    points += 10
    wb.open ("https://www.shutterstock.com/image-vector/cool-comic-book-bubble-text-pop-342092249")

t.sleep (5)
food = pg.prompt ("What is your favorite food?").lower()
if food == "tacos":
    pg.alert ("I love tacos!")
    points += 83
    wb.open ("https://giphy.com/explore/dancing-taco")
elif food == "hamburgers":
    pg.alert ("Hamburgers are my favorite!")
    points += 92
    wb.open ("https://www.google.com/imgres?imgurl=https%3A%2F%2Fdata.whicdn.com%2Fimages%2F39709705%2Flarge.jpg&imgrefurl=https%3A%2F%2Fweheartit.com%2Fentry%2F39709705&docid=ZXFjQWpCS-kmmM&tbnid=N7xn_Xd2SlhsbM%3A&vet=10ahUKEwjh0JW75Y3eAhWhmeAKHbksBQYQMwhOKAMwAw..i&w=500&h=335&bih=616&biw=681&q=yummy%20hamburger&ved=0ahUKEwjh0JW75Y3eAhWhmeAKHbksBQYQMwhOKAMwAw&iact=mrc&uact=8")
elif food == "pizza":
    pg.alert ("Pizza is alright")
    points -= 70
    wb.open ("https://friendlystock.com/product/winking-and-smiling-pizza-emoji/")
elif food == "hotdogs":
    pg.alert ("hotdogs are great for you!")
    points += 100
    wb.open ("http://dogbuns.com/Ourbuns.html")
elif food == "corndogs":
    pg.alert ("corndogs are super yummy")
    points += 13
    wb.open ("https://www.kidrobot.com/products/yummy-world-medium-corn-dog-food-plush")
elif food == "french fries":
    pg.alert ("Those are my favorite food")
    points += 4567
    wb.open ("https://www.google.com/search?q=french+fries&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi6kZO4r5_eAhVKJt8KHRawBt8Q_AUIDigB&biw=831&bih=616")
else:
    pg.alert ("Your favorite food is " + food)
    points += 91
    wb.open ("https://www.google.com/imgres?imgurl=https%3A%2F%2Ffoodrevolution.org%2Fwp-content%2Fuploads%2F2018%2F04%2Fblog-featured-diabetes-20180406-1330.jpg&imgrefurl=https%3A%2F%2Ffoodrevolution.org%2Fblog%2Fhow-to-eat-to-prevent-diabetes%2F&docid=lxGvikVaP1JDkM&tbnid=9k7oOgrIsEGl_M%3A&vet=10ahUKEwiA-YKg5o3eAhURZd8KHeiXDHkQMwhzKAowCg..i&w=2300&h=1225&bih=616&biw=681&q=food&ved=0ahUKEwiA-YKg5o3eAhURZd8KHeiXDHkQMwhzKAowCg&iact=mrc&uact=8")

t.sleep (5)
name = pg.prompt ("What's your name?").lower()
if name == "bridget":
    pg.alert ("That's a cool name")
    points += 18
    wb.open ("https://www.google.com/search?q=bridget+in+script&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjbr5TbwvfeAhUSn-AKHbK3DEUQ_AUIDigB&biw=1366&bih=626#imgrc=Vjse-SsN8aqTZM:")
elif name == "chandler":
    pg.alert ("My friends name is Chandler!")
    points += 29
    wb.open ("http://www.vulture.com/2017/03/here-is-matthew-perrys-favorite-chandler-bing-one-liner.html")
elif name == "campbell":
    pg.alert ("Thats an ok name")
    points -= 37
    wb.open ("https://www.denverpost.com/2017/02/07/campbells-soup-business-future/")
elif name == "winnie":
    pg.alert ("I was going to be named that")
    points += 1298
    wb.open ("https://digitalcitizen.ca/2010/12/04/cartoons-pictures-for-facebook-profile-pics-campaign-against-child-abuse/winne-the-pooh/")
elif name == "peyton":
    pg.alert ("Cool name")
    points += 297
    wb.open ("https://photo-forum.net/en/index.php?APP_ACTION=GALLERY_IMAGE&IMAGE_ID=808289")
elif name == "kate":
    points += 566
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=831&bih=616&tbm=isch&sa=1&ei=8ozQW5y1CKub_QbvlZjgCw&q=kate&oq=kate&gs_l=img.3..0i67l2j0j0i67j0l3j0i67j0l2.23328.24896..25174...0.0..0.69.533.10......0....1..gws-wiz-img.......0i8i30j0i24.E-c4iZVbEKk")
else:
    pg.alert ("Your name is " + name)
    points += 102
    wb.open ("http://www.babynamewizard.com/international-names-lists-popular-names-from-around-the-world")

t.sleep (5)
candy = pg.prompt ("What's your favorite candy?") .lower()
if candy == "sour patch":
    pg.alert ("I LOVE those!")
    points += 184
    wb.open ("http://www.costume-works.com/sour-patch-kids.html")
elif candy == "candycorn":
    pg.alert ("That's my favorite, too")
    points += 108
    wb.open ("https://www.amazon.com/Childs-Toddler-Candy-Corn-Costume/dp/B001FVSYWO")
elif candy == "crunch":
    pg.alert ("My friend loves those")
    points -= 95
    wb.open ("https://www.pinterest.com/pin/52635889366246982/")
elif candy == "kit kat":
    pg.alert ("Those are ok")
    points -= 986
    wb.open ("http://www.charactercentral.net/C1800_Characters_Other_KitKat.aspx")
elif candy == "twix":
    pg.alert ("Those are my least favorite")
    points -= 239
    wb.open ("https://www.walmart.com/ip/Twix-Caramel-Fun-Size-Chocolate-Cookie-Halloween-Candy-Bar-20-62-Oz/50861019")
elif candy == "skittles":
    pg.alert ("those are so colorful")
    points =+ 9365
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=831&bih=616&tbm=isch&sa=1&ei=DI3QW7CPEoOb_Qadr42wBQ&q=skittles&oq=skittles&gs_l=img.3..0l10.92856.93520..93585...0.0..0.61.390.8......0....1..gws-wiz-img.......0i67.DnBU8jQ0SjM")
else:
    pg.alert ("Your favorite candy is " + candy)
    points += 946
    wb.open ("https://www.google.com/imgres?imgurl=https%3A%2F%2Fs18670.pcdn.co%2Fwp-content%2Fuploads%2F10-Best-Halloween-Candy-Experiments.jpg&imgrefurl=https%3A%2F%2Fwww.weareteachers.com%2Fhalloween-candy-experiments%2F&docid=iDQ8WxSgjoAvTM&tbnid=Db_lHcCc7y_GEM%3A&vet=10ahUKEwjq2YH76I3eAhXLUt8KHaAxD7QQMwhzKAswCw..i&w=800&h=450&bih=616&biw=831&q=candy&ved=0ahUKEwjq2YH76I3eAhXLUt8KHaAxD7QQMwhzKAswCw&iact=mrc&uact=8")

t.sleep (5)
movie = pg.prompt ("What is your favorite movie?") .lower()
if movie == "princess bride":
    pg.alert ("That is my favorite movie!")
    points += 368
    wb.open ("https://www.youtube.com/watch?v=OfcILoREum8")
elif movie == "diary of a whimpy kid":
    pg.alert ("that is an okay movie")
    points -= 835
    wb.open ("https://www.youtube.com/watch?v=T1x0bYr0bgY")
elif movie == "frozen":
    pg.alert ("great movie!")
    points += 14
    wb.open ("https://www.youtube.com/watch?v=TbQm5doF_Uc")
elif movie == "wild child":
    pg.alert ("cool")
    points += 73
    wb.open ("https://www.youtube.com/watch?v=NdYXF6JESPc")
elif movie == "sleeping beauty":
    pg.alert ("that is an alright movie")
    points -= 1000
    wb.open ("https://www.youtube.com/watch?v=CfsyUyi_FJM")
elif movie == "mamma mia":
    pg.alert ("that is a great movie")
    points += 835
    wb.open ("https://www.youtube.com/watch?v=8RBNHdG35WY")
else:
    pg.alert ("Your favorite movie is " + movie)
    points += 846
    wb.open ("https://www.google.com/search?q=every+movie+ever+made&rlz=1C1GCEA_enUS752US752&oq=every+movie+ever+made&aqs=chrome..69i57j0l5.3482j0j4&sourceid=chrome&ie=UTF-8")

t.sleep (5)
book = pg.prompt ("What is your favorite book?") .title()
if book == "The Fault In Our Stars":
    pg.alert ("I just read that!")
    points += 93
    wb.open ("https://www.youtube.com/watch?v=9ItBvH5J6ss")
elif book == "Into The Wild":
    pg.alert ("I read that over summer!")
    points -= 10
    wb.open ("https://www.amazon.com/gp/product/B0016OLC5Q/ref=atv_feed_catalog")
elif book == "Endangered":
    pg.alert ("I am doing a book talk on that!")
    points += 73
    wb.open ("https://play.google.com/store/books/details?id=6q5sc8iwuRIC&source=productsearch&utm_source=HA_Desktop_US&utm_medium=SEM&utm_campaign=PLA&pcampaignid=MKTAD0930BO1&gclid=EAIaIQobChMIzL_l8-a_3gIVF1qGCh2mVwG5EAQYAiABEgKxTPD_BwE&gclsrc=aw.ds")
elif book == "Everything Everything":
    pg.alert ("I loved the movie!")
    points += 96
    wb.open ("https://www.youtube.com/watch?v=42KNwQ6u42U")
elif book == "Solo":
    pg.alert ("I love the author, Kwame Alexander!")
    points = 28
    wb.open ("https://play.google.com/store/books/details?id=jb94DQAAQBAJ&source=productsearch&utm_source=HA_Desktop_US&utm_medium=SEM&utm_campaign=PLA&pcampaignid=MKTAD0930BO1&gclid=EAIaIQobChMI8pLZgui_3gIVAahpCh3aegsTEAQYAyABEgKEsvD_BwE&gclsrc=aw.ds")
elif book == "To All The Boys I Loved Before":
    pg.alert ("That is my favorite book and movie of all time!")
    points +=839
    wb.open ("https://www.youtube.com/watch?v=555oiY9RWM4")
else:
    pg.alert ("Your favorite book is " + book)
    points += 10
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&ei=qo_hW-OHDor4jwSxh4aQDA&q=the+best+books+of+all+time&oq=the+best+books+of+all+time&gs_l=psy-ab.3..0l5j0i22i30l5.62.2054..2143...0.0..0.145.1000.13j1......0....1..gws-wiz.......0i71.B-Cyr0ZvFwE")
pg.alert (points)
