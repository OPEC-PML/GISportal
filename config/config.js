/*------------------------------------*\
   Configuration
   This file is for the configuration
   of the GIS Portal.

   browseCategories - Used to define
   which categories to be shown in the
   browse panel. This is currently
   limited to 2.
\*------------------------------------*/



gisportal.config = {
   siteMode: "production", //(development|production)
   browseCategories : {
      "Ecosystem_Element" : "Ecosystem </br> Indicator",
      "region": "Regional </br> Seas",
      "MSFD" : "EU MSFD </br> Descriptor"
   },
   paths: {
      graphServer: 'http://portal.marineopec.eu/plotting',
      middlewarePath: '/service'
   },

   // Should layers auto scale by default
   autoScale: true,

   requiresTermsAndCondictions: true,

   countryBorder : {
      'defaultLayer' : 'countries_all_white',      // (countries_all_white|countries_all_black|countries_all_blue)
      'alwaysVisible' : false                      // (true|false)  > If true the defaultLayer will be visible at page load
   },
   defaultBaseMap: 'EOX',

    homepageSlides: [
      "img/homepage-slides/opec1.jpg",
      "img/homepage-slides/opec2.jpg",
      "img/homepage-slides/opec3.jpg",
      "img/homepage-slides/opec4.jpg",
      "img/homepage-slides/opec5.jpg",
      "img/homepage-slides/opec6.jpg",
      "img/homepage-slides/opec7.jpg"
   ],

   // Deny access to older browsers
   // none=Allow, advisory=Tell them only, strict=Stop them
   browserRestristion: "strict" //(none|advisory|strict)

};

