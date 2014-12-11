/*------------------------------------*\
    Selection Tools
    This file is for selecting features
    on the map, such as rectangles etc.
    It is separate from indicatorsPanel
    to make the code more future-proof.
\*------------------------------------*/

gisportal.selectionTools = {};

gisportal.selectionTools.init = function() {
   gisportal.selectionTools.initDOM();
   var vectorLayer = new OpenLayers.Layer.Vector('POI Layer', {

      style: {
         strokeColor: 'white',
         fillColor: 'green',
         strokeWidth: 2,
         fillOpacity: 0.3,
         pointRadius: 5
      },
      preFeatureInsert: function(feature) {
         this.removeAllFeatures();
      },
      onFeatureInsert: function(feature) {
         gisportal.selectionTools.ROIAdded(feature);
         gisportal.selectionTools.closeAllHelp();
      },
      rendererOptions: {
         zIndexing: true
      },
      renderers: ['Canvas', 'VML']
   });
   vectorLayer.events.on({
      'featureover': function(evt) {

         var v = evt.feature;
         if (!v.popid) {
            console.log(v.geometry);
            var coord = new OpenLayers.LonLat(v.geometry.bounds.right, v.geometry.bounds.top);
            var pixels = map.getPixelFromLonLat(coord);
            console.log(pixels);
            var _id = Date.now();
            var pop = $('<div>', {
               id: _id
            }).css({
               position: "absolute",
               top: pixels.y,
               left: pixels.x,

            }).addClass('marker_close').append($('<span></span>').addClass('btn icon-filled-arrow-delete-1 icon-btn panel-icon-tab right-icon').css({
               "font-size": "2em"
            })).on('click', function(e) {
               $(this).remove();
               vectorLayer.removeFeatures(v);
               $('.js-coordinates').val('');
               console.log('i clicked the thing"');
            });
            $('body').append(pop);
            v.popid = _id;

         } // end if

      },
      'featureout': function(evt) {
         var feature = evt.feature;
         console.log(feature.popid);
         setTimeout(function() {
            console.log('removing :' + feature.popid);
            $('#' + feature.popid).remove();
            delete feature.popid;
         }, 4000);
      },
      "featureselected": function(e) {
         //here I need to get XY
         //something like the code below 
         //(it doesn't work but clearly explains what my idea is)           
         console.log(e.xy);

      }
   });
   vectorLayer.controlID = "poiLayer";
   vectorLayer.displayInLayerSwitcher = false;

   map.addLayer(vectorLayer);

   gisportal.mapControls.box = new OpenLayers.Control.DrawFeature(vectorLayer, OpenLayers.Handler.RegularPolygon, {
      handlerOptions: {
         sides: 4,
         irregular: true,
         persist: false
      }
   });

   gisportal.mapControls.polygon = new OpenLayers.Control.DrawFeature(vectorLayer, OpenLayers.Handler.Polygon, {
      handlerOptions: {
         persist: false
      }
   });

   gisportal.mapControls.line = new OpenLayers.Control.DrawFeature(vectorLayer, OpenLayers.Handler.Path, {
      handlerOption: {
         persist: false
      }
   });
   gisportal.wkt = new OpenLayers.Format.WKT();

   map.addControls([gisportal.mapControls.box, gisportal.mapControls.polygon, gisportal.mapControls.line]);

};

gisportal.selectionTools.initDOM = function() {
   $('.js-indicators').on('change', '.js-coordinates', gisportal.selectionTools.updateROI);

   $('.js-indicators').on('click', '.js-draw-box', function() {
      //gisportal.selectionTools.polygonBoxHelp();
      gisportal.selectionTools.toggleTool('box');
   });
   $('.js-indicators').on('click', '.js-draw-polygon', function() {
      gisportal.selectionTools.polygonHelp();
      gisportal.selectionTools.toggleTool('polygon');
   });
   $('.js-indicators').on('click', '.js-draw-line', function() {
      console.log('clicked the line draw');
      gisportal.selectionTools.toggleTool('line');
   });

   $('body').on('click', '#bbox_help > #closePolyHelp', function(ev) {
      console.log('clicked 1');
      gisportal.selectionTools.closeAllHelp('BBox');
   });
   $('body').on('click', '#polygon_help > #closePolyHelp', function(ev) {
      console.log('clicked 2');
      gisportal.selectionTools.closeAllHelp('Poly');
   });
};

gisportal.selectionTools.toggleBboxDisplay = function() {

   $('.coordinates').disabled();



};

gisportal.selectionTools.helpIsActive = false;



gisportal.selectionTools.helpRequiredBBox = function() {
   return gisportal.storage.get('helpRequiredBBox', true);
};

gisportal.selectionTools.helpRequiredPoly = function() {
   return gisportal.storage.get('helpRequiredPoly', true);
};

// currently not used as not required for OPEC
gisportal.selectionTools.polygonBoxHelp = function() {

   if (gisportal.selectionTools.helpRequiredBBox()) {
      if (gisportal.selectionTools.helpIsActive) {
         gisportal.selectionTools.closeAllHelp('BBox');
      }
      gisportal.selectionTools.helpIsActive = true;
      var renderedTooltip = gisportal.templates['bbox-help']();
      $('body').append($(renderedTooltip));


   }
};

gisportal.selectionTools.polygonHelp = function() {
   if (gisportal.selectionTools.helpRequiredPoly()) {

      if (gisportal.selectionTools.helpIsActive) {
         gisportal.selectionTools.closeAllHelp('Poly');
      }
      gisportal.selectionTools.helpIsActive = true;
      var renderedTooltip = gisportal.templates['polygon-help']();
      $('body').append($(renderedTooltip));

   }
};

gisportal.selectionTools.closeAllHelp = function(type) {
   if (type) {
      if ($('#noShow')[0].checked) {
         gisportal.storage.set('helpRequired' + type, false);
      }
   }
   gisportal.selectionTools.helpIsActive = false;
   $('.polygon_help').remove();
};

gisportal.selectionTools.getActiveControl = function() {
   activeControl = '';
   for (var key in gisportal.mapControls) {
      if (gisportal.mapControls[key].active) {
         activeControl = key;
      }
   }
   return activeControl;
};

gisportal.selectionTools.toggleTool = function(tool) {
   var vectorLayer = map.layers[map.layers.length - 1];

   var isActive = false;
   for (var key in gisportal.mapControls) {
      var control = gisportal.mapControls[key];
      if (key === tool) {
         control.activate();
         isActive = true;
      } else {
         control.deactivate();
      }
   }

   if (!isActive) {
      console.log('There were no tools toggled, so pan has been activated');
      gisportal.mapControls['pan'].activate();
   }

   map.ROI_Type = tool;

};

gisportal.selectionTools.updateROI = function() {
   var values = $(this).val().split(',');
   values[0] = gisportal.utils.clamp(values[0], -180, 180); // Long
   values[2] = gisportal.utils.clamp(values[2], -180, 180); // Long
   values[1] = gisportal.utils.clamp(values[1], -90, 90); // Lat
   values[3] = gisportal.utils.clamp(values[3], -90, 90); // Lat
   $(this).val(values[0] + ',' + values[1] + ',' + values[2] + ',' + values[3]);
   var feature = new OpenLayers.Feature.Vector(new OpenLayers.Bounds(values[0], values[1], values[2], values[3]).toGeometry());

   // map.layers corrosponds to layers of the map,
   // such as base layer and vector, not indicators on the map
   var vectorLayer = map.layers[map.layers.length - 1];
   feature.layer = vectorLayer;
   var features = vectorLayer.features;
   if (features[0]) vectorLayer.features[0].destroy();
   vectorLayer.features[0] = feature;
   vectorLayer.redraw();
};

gisportal.currentSelectedRegion = "";
gisportal.selectionTools.ROIAdded = function(feature) {
   var feature_type = map.ROI_Type;
   var bounds;
   if (feature_type === "polygon") {
      console.log('generation polygon WKT');
      var wkt_feature = gisportal.wkt.write(feature);
      console.log(wkt_feature);
      bounds = feature.geometry.bounds;

      wkt_feature = wkt_feature.replace(/[\d\.]+/g, function(num) {
         return Math.round(num * 1000) / 1000;
      });

      gisportal.currentSelectedRegion = wkt_feature;
      $('.js-coordinates').val(wkt_feature);
      $('.bbox-info').toggleClass('hidden', false);
   } else if (feature_type === 'line') {
      console.log('generation line WKT');
      var wkt_feature = gisportal.wkt.write(feature);
      console.log(wkt_feature);
      bounds = feature.geometry.bounds;

      wkt_feature = wkt_feature.replace(/[\d\.]+/g, function(num) {
         return Math.round(num * 1000) / 1000;
      });

      gisportal.currentSelectedRegion = wkt_feature;
      $('.js-coordinates').val(wkt_feature);
      $('.bbox-info').toggleClass('hidden', false);
   } else {
      bounds = feature.geometry.bounds;
      var coords = "";
      if (bounds) {
         coords += bounds.left + ",";
         coords += bounds.bottom + ",";
         coords += bounds.right + ",";
         coords += bounds.top;

         coords = coords.replace(/[\d\.]+/g, function(num) {
            return Math.round(num * 1000) / 1000;
         });

         gisportal.currentSelectedRegion = coords;
         $('.js-coordinates').val(coords);
         $('.bbox-info').toggleClass('hidden', false);
      }
   }
   this.toggleTool('pan'); // So that people don't misclick



   // Get the geometry of the drawn feature
   var geom = new OpenLayers.Geometry();
   geom = feature.geometry;

   var area_deg, area_km, height_deg, width_deg, height_km, width_km, radius_deg, ctrLat, ctrLon = 0;

   if (feature_type !== '' && feature_type != 'point' && bounds) {
      area_deg = geom.getArea();
      area_km = (geom.getGeodesicArea() * 1e-6);
      height_deg = bounds.getHeight();
      width_deg = bounds.getWidth();
      // Note - to get values in true ellipsoidal distances, we need to use Vincenty functions for measuring ellipsoidal
      // distances instead of planar distances (http://www.movable-type.co.uk/scripts/latlong-vincenty.html)
      ctrLon = geom.getCentroid().x;
      ctrLat = geom.getCentroid().y;
      height_km = OpenLayers.Util.distVincenty(new OpenLayers.LonLat(ctrLon, bounds.top), new OpenLayers.LonLat(ctrLon, bounds.bottom));
      width_km = OpenLayers.Util.distVincenty(new OpenLayers.LonLat(bounds.left, ctrLat), new OpenLayers.LonLat(bounds.right, ctrLat));
      radius_deg = ((bounds.getWidth() + bounds.getHeight()) / 4);

      var pretty_height_km, pretty_width_km, pretty_area_km
         // because not all browsers support Intl.NumberFormat ...
      try {
         pretty_height_km = new Intl.NumberFormat("en-GB", {
            maximumFractionDigits: 2
         }).format(height_km);
      } catch (e) {
         pretty_height_km = height_km.toPrecision(4);
      }
      try {
         pretty_width_km = new Intl.NumberFormat("en-GB", {
            maximumFractionDigits: 2
         }).format(width_km);
      } catch (e) {
         pretty_width_km = width_km.toPrecision(4);
      }
      try {
         pretty_area_km = new Intl.NumberFormat("en-GB", {
            maximumFractionDigits: 0
         }).format(area_km);
      } catch (e) {
         pretty_area_km = area_km.toPrecision(4);
      }

   }

   switch (feature_type) {
      case 'box':
         $('.js-bbox-width').html(pretty_width_km + ' km');
         $('.js-bbox-height').html(pretty_height_km + ' km');
         $('.js-bbox-area').html(pretty_area_km + ' km<sup>2</sup>');
         break;
      case 'point':
         // set the .bbox-info div to show lat/long
         break;
      case 'circle':
         // set the .bbox-info div to show lat/long of the centre, the radius, width, height and area
         break;
      case 'polygon':
         // set the .bbox-info div to show the centroid lat/long and area
         $('.js-bbox-width').html('');
         $('.js-bbox-height').html('');
         $('.js-bbox-area').html(pretty_area_km + ' km<sup>2</sup>');
         break;
   }



};