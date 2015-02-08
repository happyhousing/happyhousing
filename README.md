# Zillow HackHouse Hackathon: Happy Housing

The purpose of this app is to help recent immigrants of Seattle find affordable housing close to either their workplace, home, or preferred living location.

This application was developed on from February 6, 2015 to February February 8, 2015 for the [Hack Housing: Empowering Smarter Decisions – A Weekend Hackathon](http://investors.zillow.com/releasedetail.cfm?ReleaseID=892685).

![Happy housing](https://github.com/happyhousing/happyhousing/blob/master/homeful/media/images/Happyhousing_logo.png)

Our app is live at http://hh-helptheworld.herokuapp.com/homeful/. 

## Challenge and Approach

Our submission is to address the following Low Income Renter challenge #3:
- where are the multi-family communities that accept my rental voucher, and is there availability in the communities?- 
- Simple, consumer-friendly solutions to narrow their options, find available units, submit necessary information and connect with service providers. 
- They can find this site by visiting the public library, or a mobile site.

1.  Open our [HappyHousing webpage](http://hh-helptheworld.herokuapp.com/homeful/)
2.  Select language
3.  Enter zip code
4.  Select the number of rooms you need.

Our approach for satisfying this challenge was to:

- Analyze current low income housing opportunities such as HUD, Seattle public housing, and Section 8.
- for much of these opportunities we realize that there is a waiting list.
- We identified that our customers would like recommendations on housing near their work or home.
- The application can be customize to their preferred language
- We pulled from the [Multi Family Data](http://zillowhack.hud.opendata.arcgis.com/datasets/c55eb46fbc3b472cabd0c2a41f805261_0)
- We pulled from the [Fair Market Rent Data](http://zillowhack.hud.opendata.arcgis.com/datasets/e29dca94b6924766a124d7c767e03b75_0)
- We use the FMR to give the search an idea of the price range for the apartments
- We use the multi-family data to provide contact information and addresses to allow in person or telephone contact.
- we also added easy to understand images for reading challenged, and native language customization.  

## Team Members

Our team is comprised of:

- [@qayshp](http://github.com/qayshp) - Qays Poonawala
- [@YasharF](http://github.com/YasharF) - Yashar Fakhari
- [@ega123](http://github.com/ega123) - Shiirevjamts Munkhbat
- [@alyeung](http://github.com/alyeung) - Allan Yeung
- [Tuvshin](http://github.com/JFKHD!!!!!#*!) - Tuvshin Erdenebaatar

## Technologies, APIs, and Datasets Utilized

We made use of:

- [django](http://djangoproject.com)
- python request library
- Heroku
- JSON library
- [Google Maps](https://mapsengine.google.com/map/u/0/)
- HTML5
- [JetStrap](https://jetstrap.com)
- Google Translate plug-in

- [Multi Family Data](http://zillowhack.hud.opendata.arcgis.com/datasets/c55eb46fbc3b472cabd0c2a41f805261_0)
- [Fair Market Rent Data](http://zillowhack.hud.opendata.arcgis.com/datasets/e29dca94b6924766a124d7c767e03b75_0)

## Contributing

In order to build and run our app:
1)  Download source to your github.
2)  setup a heroku account.
3)  link github to heroku for continuous build.
4)  open up your heroku weblink.


Our code is licensed under the [MIT License](LICENSE.md). Pull requests will be accepted to this repo, pending review and approval.
