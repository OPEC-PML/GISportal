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
   browseCategories : {
      "Ecosystem_Element" : "Ecosystem",
      "region": "Region",
      "MSFD" : "MSFD"
   },
   popularIndicators : [
      "Heterotrophic flagellates biomass", "Net Primary Production", "Oxygen", "Temperature"
   ],
   defaultStates: [
      {
         "name" : "Cod in the North East Atlantic",
         "url" : "http://portaldev.marineopec.eu/?state=b8czastdcoioi"
      },
      {
         "name" : "Seasonal Changes in Chlorophyll levels in the Med",
         "url" : "http://portaldev.marineopec.eu/?state=a9bmsjjtthehe"
      },
      {
         "name" : "Interannual Nitrogen in the Baltic",
         "url" : "http://portaldev.marineopec.eu/?state=c7ebs12wvvmvm"
      },
      {
         "name" : "Summer zooplankton growth in the Black Sea",
         "url" : "http://portaldev.marineopec.eu/?state=bqua1n6lk2yky"
     }
   ],
   analytics: {
      active: true,
      UATrackingId: 'UA-52647976-2',
      
      customDefinitions: {
         layerChange: {
            /**
            *  Layout:
            *     (cd|cm){{index}} : ( function(){} | predefined_function_name | string )
            *  Example:
            *     cd2 : 'indicator_name' //Call the indicator_name default function and apply to definition 2
            *     cd3 : function( indicator ){ return indicator.name + "-" + indicator.id  } // Sets definition 3 to the indicator name + id,
            *     cm1 : 1 //Sets metric 1 to the value of one
            */
            "cd8": 'indicator_name',
            "cd9": 'indicator_id',
            "cd2": 'indicator_region',
            "cd3": 'indicator_interval',
            "cd7": 'indicator_confidence',
            "cd4": 'indicator_elevation',
            "cd5": 'indicator_layer_style',
            "cd10":'indicator_year',
            'cm2': 1 // Used in layer
         },
         
         selectionBoxDrawn: {
            "cd8": 'indicator_name',
            "cd9": 'indicator_id',
            "cd2": 'indicator_region',
            "cd3": 'indicator_interval'
         },
         
         selectionBoxTyped: {
            "cd8": 'indicator_name',
            "cd9": 'indicator_id',
            "cd2": 'indicator_region',
            "cd3": 'indicator_interval'
         },
         
         dateRangeUsed: {
            "cd8": 'indicator_name',
            "cd9": 'indicator_id',
            "cd2": 'indicator_region',
            "cd3": 'indicator_interval'
         },
         
         createGraph: {
            "cd8": 'indicator_name',
            "cd9": 'indicator_id',
            "cd2": 'indicator_region',
            "cd3": 'indicator_interval',
            "cd6": 'graph_type',
            'cm1': 1  // Used in graph
         },
         
         
         //Does not a get a true gisportal.layer. Only: { 'name': 'Oxygen' }.
         selectLayer: {
            "cd8": 'indicator_name'
         },
         
         //Does not a get a true gisportal.layer. Only: { 'name': 'Oxygen' }.
         deselectLayer: {
            "cd8": 'indicator_name'
         },
         
         
         showLayer: {
            "cd8": 'indicator_name'
         },
         
         hideLayer: {
            "cd8": 'indicator_name'
         },
         
         timelineUpdate: {
            "cd10": 'timeline_year'
         }
         
      }
      
   }
};
