layers = [
    {
        "indicators": {
            "chl": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Chlorophyll", 
                "region": "Mediterranean Sea"
            }, 
            "mesozooplankton": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Zooplankton", 
                "region": "Mediterranean Sea"
            }, 
            "mld": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrographical Conditions"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Mixed Layer Depth", 
                "region": "Mediterranean Sea"
            }, 
            "netPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Primary Production", 
                "region": "Mediterranean Sea"
            }, 
            "nitrate": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Nitrate", 
                "region": "Mediterranean Sea"
            }, 
            "oxygen": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Oxygen", 
                "region": "Mediterranean Sea"
            }, 
            "pH": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Chemistry", 
                "MSFD": [
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "pH", 
                "region": "Mediterranean Sea"
            }, 
            "pco2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "pCO2", 
                "region": "Mediterranean Sea"
            }, 
            "phosphate": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Phosphate", 
                "region": "Mediterranean Sea"
            }, 
            "salinity": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biological Diversity", 
                    "Hydrographical Conditions"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Salinity", 
                "region": "Mediterranean Sea"
            }, 
            "silicate": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity"
                ], 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Silicate", 
                "region": "Mediterranean Sea"
            }, 
            "temperature": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "contact": "Kostas Tsiaras", 
                "interval": "Monthly", 
                "model": "POM-ERSEM", 
                "niceName": "Temperature", 
                "region": "Mediterranean Sea"
            }
        }, 
        "name": "hcmr", 
        "options": {
            "positive": "up", 
            "providerShortTag": "HCMR"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "http://ogc.hcmr.gr:8080/thredds/wcs/POMERSEM_MED_MONTHLY?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "http://ogc.hcmr.gr:8080/thredds/wms/POMERSEM_MED_MONTHLY?"
            }
        }
    }, 
    {
        "indicators": {
            "Cod__adult_": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Jonathan Beecham", 
                "interval": "Daily", 
                "model": "POLCOMS-ERSEM-Ecospace - Cefas North Sea Model", 
                "niceName": "Adult Cod", 
                "region": "North East Atlantic"
            }, 
            "Herring__adult_": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Jonathan Beecham", 
                "interval": "Daily", 
                "model": "POLCOMS-ERSEM-Ecospace - Cefas North Sea Model", 
                "niceName": "Adult Herring", 
                "region": "North East Atlantic"
            }, 
            "Herring__juvenile_0__1_": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Jonathan Beecham", 
                "interval": "Daily", 
                "model": "POLCOMS-ERSEM-Ecospace - Cefas North Sea Model", 
                "niceName": "Juvenile Herring", 
                "region": "North East Atlantic"
            }, 
            "Juvenile_Cod_0_2__0_40cm_": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Jonathan Beecham", 
                "interval": "Daily", 
                "model": "POLCOMS-ERSEM-Ecospace - Cefas North Sea Model", 
                "niceName": "Juvenile Cod", 
                "region": "North East Atlantic"
            }, 
            "Plaice": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Jonathan Beecham", 
                "interval": "Daily", 
                "model": "POLCOMS-ERSEM-Ecospace - Cefas North Sea Model", 
                "niceName": "Plaice", 
                "region": "North East Atlantic"
            }, 
            "Sandeels": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Jonathan Beecham", 
                "interval": "Daily", 
                "model": "POLCOMS-ERSEM-Ecospace - Cefas North Sea Model", 
                "niceName": "Sandeels", 
                "region": "North East Atlantic"
            }, 
            "Seabirds": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Jonathan Beecham", 
                "interval": "Daily", 
                "model": "POLCOMS-ERSEM-Ecospace - Cefas North Sea Model", 
                "niceName": "Seabirds", 
                "region": "North East Atlantic"
            }
        }, 
        "name": "cefas", 
        "options": {
            "positive": "down", 
            "providerShortTag": "Cefas"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/CEFAS_GEN_HC?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/CEFAS_GEN_HC?"
            }
        }
    }, 
    {
        "indicators": {
            "Chloro": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Chlorophyll", 
                "region": "Baltic Sea"
            }, 
            "DIN": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Nitrate", 
                "region": "Baltic Sea"
            }, 
            "DIP": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Phosphate", 
                "region": "Baltic Sea"
            }, 
            "MLD": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Mixed Layer Depth", 
                "region": "Baltic Sea"
            }, 
            "Oxy": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Oxygen", 
                "region": "Baltic Sea"
            }, 
            "Ph": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Chemistry", 
                "MSFD": [
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "pH", 
                "region": "Baltic Sea"
            }, 
            "Salt": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Salinity", 
                "region": "Baltic Sea"
            }, 
            "Temp": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Temperature", 
                "region": "Baltic Sea"
            }, 
            "Zooplank": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Zhenwen Wan", 
                "interval": "Monthly", 
                "model": "HBM-ERGOM", 
                "niceName": "Zooplankton", 
                "region": "Baltic Sea"
            }
        }, 
        "name": "dmi", 
        "options": {
            "positive": "up", 
            "providerShortTag": "DMI"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/DMI_GEN?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/DMI_GEN?"
            }
        }
    }, 
    {
        "indicators": {
            "Chl": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Chlorophyll", 
                "region": "North East Atlantic"
            }, 
            "DIN": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Nitrate", 
                "region": "North East Atlantic"
            }, 
            "DIP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Phosphate", 
                "region": "North East Atlantic"
            }, 
            "DISi": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Silicate", 
                "region": "North East Atlantic"
            }, 
            "MLD": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrographical Conditions"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Mixed Layer Depth", 
                "region": "North East Atlantic"
            }, 
            "N:P": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Nitrate/Phosphate ratio", 
                "region": "North East Atlantic"
            }, 
            "N:Si": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Nitrate/Silicate ratio", 
                "region": "North East Atlantic"
            }, 
            "O2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Oxygen", 
                "region": "North East Atlantic"
            }, 
            "PEA": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrographical Conditions"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Potential Energy Anomaly", 
                "region": "North East Atlantic"
            }, 
            "Pc": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Phytoplankton", 
                "region": "North East Atlantic"
            }, 
            "S": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biological Diversity", 
                    "Hydrographical Conditions"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Salinity", 
                "region": "North East Atlantic"
            }, 
            "T": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biological Diversity", 
                    "Hydrographical Conditions"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Temperature", 
                "region": "North East Atlantic"
            }, 
            "Zc": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Zooplankton", 
                "region": "North East Atlantic"
            }, 
            "euphDepth": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biological Diversity", 
                    "Hydrographical Conditions"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Euphotic depth", 
                "region": "North East Atlantic"
            }, 
            "netPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "Primary Production", 
                "region": "North East Atlantic"
            }, 
            "pCO2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "contact": "Stefano Ciavatta", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM", 
                "niceName": "pCO2", 
                "region": "North East Atlantic"
            }
        }, 
        "name": "pml_monthly", 
        "options": {
            "positive": "down", 
            "providerShortTag": "PML"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/PML_GEN_M?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/PML_GEN_M?"
            }
        }
    }, 
    {
        "indicators": {
            "Ammonia": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Ammonia", 
                "region": "Mediterranean Sea"
            }, 
            "NPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Foodwebs"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Primary Production", 
                "region": "Mediterranean Sea"
            }, 
            "Nitrate": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Nitrate", 
                "region": "Mediterranean Sea"
            }, 
            "Oxygen": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Oxygen", 
                "region": "Mediterranean Sea"
            }, 
            "Phosphate": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Phosphate", 
                "region": "Mediterranean Sea"
            }, 
            "R_NO3_PHOS": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Nitrate/Phosphate ratio", 
                "region": "Mediterranean Sea"
            }, 
            "R_NO3_SIO4": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Nitrate/Silicate ratio", 
                "region": "Mediterranean Sea"
            }, 
            "Silicate": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Silicate", 
                "region": "Mediterranean Sea"
            }, 
            "Totchl": {
                "Confidence": "High", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Foodwebs"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Chlorophyll", 
                "region": "Mediterranean Sea"
            }, 
            "TotphytoC": {
                "Confidence": "High", 
                "Ecosystem_Element": "Plankton", 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Phytoplankton", 
                "region": "Mediterranean Sea"
            }, 
            "Totzoo": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Zooplankton", 
                "region": "Mediterranean Sea"
            }, 
            "pCO2": {
                "Confidence": "High", 
                "Ecosystem_Element": "Gases", 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "pCO2", 
                "region": "Mediterranean Sea"
            }, 
            "sal": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrographical Conditions"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Salinity", 
                "region": "Mediterranean Sea"
            }, 
            "temp": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrographical Conditions"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Temperature", 
                "region": "Mediterranean Sea"
            }
        }, 
        "name": "ogs", 
        "options": {
            "positive": "down", 
            "providerShortTag": "OGS"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/OGS-GEN?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/OGS-GEN?"
            }
        }
    }, 
    {
        "indicators": {
            "CHL": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Chlorophyll", 
                "region": "Black Sea"
            }, 
            "MLD": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrographical Conditions"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Mixed Layer Depth", 
                "region": "Black Sea"
            }, 
            "NO3": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Nitrate", 
                "region": "Black Sea"
            }, 
            "NPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Primary Production", 
                "region": "Black Sea"
            }, 
            "O2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Oxygen", 
                "region": "Black Sea"
            }, 
            "PO4": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Phosphate", 
                "region": "Black Sea"
            }, 
            "S": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biological Diversity", 
                    "Hydrographical Conditions"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Salinity", 
                "region": "Black Sea"
            }, 
            "T": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biological Diversity", 
                    "Hydrographical Conditions"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Temperature", 
                "region": "Black Sea"
            }, 
            "Z": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Plankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biological Diversity", 
                    "Foodwebs"
                ], 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "Zooplankton", 
                "region": "Black Sea"
            }, 
            "pCO2w": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "contact": "Baris Salihoglu", 
                "interval": "Monthly", 
                "model": "POM-BIMS_ECO", 
                "niceName": "pCO2", 
                "region": "Black Sea"
            }
        }, 
        "name": "metu_monthly", 
        "options": {
            "positive": "down", 
            "providerShortTag": "METU"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/IMSMETU_GEN_HC_M?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/IMSMETU_GEN_HC_M?"
            }
        }
    }, 
    {
        "indicators": {
            "U": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Sonja van Leeuwen", 
                "interval": "Monthly", 
                "model": "POLCOMS-ERSEM-Sizebased model", 
                "niceName": "Pelagic predator biomass", 
                "region": "North East Atlantic"
            }
        }, 
        "name": "cefas_monthly", 
        "options": {
            "positive": "down", 
            "providerShortTag": "Cefas"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/CEFAS_GEN_HTL?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/CEFAS_GEN_HTL?"
            }
        }
    }, 
    {
        "indicators": {
            "anchovy": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Anchovy", 
                "region": "Mediterranean Sea"
            }, 
            "sardine": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Gianpiero Cossarini", 
                "interval": "Monthly", 
                "model": "OPATM-BFM-ECOPATH with ECOSIM", 
                "niceName": "Sardine", 
                "region": "Mediterranean Sea"
            }
        }, 
        "name": "ogs_monthly", 
        "options": {
            "positive": "down", 
            "providerShortTag": "OGS"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/OGS-GEN-HTL?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/OGS-GEN-HTL?"
            }
        }
    }, 
    {
        "indicators": {
            "biomass_cod_2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Commercial Fisheries"
                ], 
                "contact": "Asbjorn Christensen", 
                "interval": "Quarterly", 
                "model": "SMS", 
                "niceName": "Juvenile Cod", 
                "region": "Baltic Sea"
            }
        }, 
        "name": "dtu", 
        "options": {
            "positive": "up", 
            "providerShortTag": "DTU"
        }, 
        "services": {
            "wcs": {
                "params": {
                    "DescribeCoverage": {
                        "SERVICE": "WCS", 
                        "request": "describeCoverage", 
                        "version": "1.0.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wcs/DTU_GEN?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/DTU_GEN?"
            }
        }
    }
]
