layers = [
    {
        "indicators": {
            "chl": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Chlorophyll", 
                "region": "Mediterranean Sea"
            }, 
            "mesozooplankton": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Zooplankton", 
                "region": "Mediterranean Sea"
            }, 
            "mld": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Mixed Layer Depth", 
                "region": "Mediterranean Sea"
            }, 
            "netPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Primary Production", 
                "region": "Mediterranean Sea"
            }, 
            "nitrate": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity"
                ], 
                "interval": "Monthly", 
                "niceName": "Nitrate", 
                "region": "Mediterranean Sea"
            }, 
            "oxygen": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Oxygen", 
                "region": "Mediterranean Sea"
            }, 
            "phosphate": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity"
                ], 
                "interval": "Monthly", 
                "niceName": "Phosphate", 
                "region": "Mediterranean Sea"
            }, 
            "salinity": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biodiversity", 
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Salinity", 
                "region": "Mediterranean Sea"
            }, 
            "silicate": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity"
                ], 
                "interval": "Monthly", 
                "niceName": "Silicate", 
                "region": "Mediterranean Sea"
            }, 
            "temperature": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biodiversity", 
                    "Hydrography"
                ], 
                "interval": "Monthly", 
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
                    "Fisheries"
                ], 
                "interval": "Daily", 
                "niceName": "Adult Cod", 
                "region": "North East Atlantic"
            }, 
            "Herbivorous_and_Omnivorous_zooplankton__copepods_": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Zooplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Daily", 
                "niceName": "Zooplankton", 
                "region": "North East Atlantic"
            }, 
            "Herring__adult_": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Fisheries"
                ], 
                "interval": "Daily", 
                "niceName": "Adult Herring", 
                "region": "North East Atlantic"
            }, 
            "Herring__juvenile_0__1_": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Fisheries"
                ], 
                "interval": "Daily", 
                "niceName": "Juvenile Herring", 
                "region": "North East Atlantic"
            }, 
            "Juvenile_Cod_0_2__0_40cm_": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Fisheries"
                ], 
                "interval": "Daily", 
                "niceName": "Juvenile Cod", 
                "region": "North East Atlantic"
            }, 
            "Phytoplankton": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Daily", 
                "niceName": "Phytoplankton", 
                "region": "North East Atlantic"
            }, 
            "Plaice": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Fisheries"
                ], 
                "interval": "Daily", 
                "niceName": "Plaice", 
                "region": "North East Atlantic"
            }, 
            "Sandeels": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Fisheries"
                ], 
                "interval": "Daily", 
                "niceName": "Sandeels", 
                "region": "North East Atlantic"
            }, 
            "Seabirds": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Fish", 
                "MSFD": [
                    "Foodwebs", 
                    "Fisheries"
                ], 
                "interval": "Daily", 
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
                "url": "https://rsg.pml.ac.uk/thredds/wcs/CEFAS_GEN_HC/OPEC_Cefas_HC.nc?"
            }, 
            "wms": {
                "params": {
                    "GetCapabilities": {
                        "SERVICE": "WMS", 
                        "request": "GetCapabilities", 
                        "version": "1.3.0"
                    }
                }, 
                "url": "https://rsg.pml.ac.uk/thredds/wms/CEFAS_GEN_HC/OPEC_Cefas_HC.nc?"
            }
        }
    }, 
    {
        "indicators": {
            "Chloro": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Chlorophyll", 
                "region": "Baltic Sea"
            }, 
            "DIN": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Nitrate", 
                "region": "Baltic Sea"
            }, 
            "DIP": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Phosphate", 
                "region": "Baltic Sea"
            }, 
            "MLD": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Mixed Layer Depth", 
                "region": "Baltic Sea"
            }, 
            "Oxy": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Oxygen", 
                "region": "Baltic Sea"
            }, 
            "Ph": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Chemistry", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "pH", 
                "region": "Baltic Sea"
            }, 
            "Salt": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Salinity", 
                "region": "Baltic Sea"
            }, 
            "Temp": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Temperature", 
                "region": "Baltic Sea"
            }, 
            "Zooplank": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Zooplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Zooplankton", 
                "region": "Baltic Sea"
            }
        }, 
        "name": "dmi", 
        "options": {
            "positive": "down", 
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
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Chlorophyll", 
                "region": "North East Atlantic"
            }, 
            "DIN": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Nitrate", 
                "region": "North East Atlantic"
            }, 
            "DIP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Phosphate", 
                "region": "North East Atlantic"
            }, 
            "DISi": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Silicate", 
                "region": "North East Atlantic"
            }, 
            "MLD": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Mixed Layer Depth", 
                "region": "North East Atlantic"
            }, 
            "N:P": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity"
                ], 
                "interval": "Monthly", 
                "niceName": "Nitrate/Phosphate ratio", 
                "region": "North East Atlantic"
            }, 
            "N:Si": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity"
                ], 
                "interval": "Monthly", 
                "niceName": "Nitrate/Silicate ratio", 
                "region": "North East Atlantic"
            }, 
            "O2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Oxygen", 
                "region": "North East Atlantic"
            }, 
            "PEA": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Potential Energy Anomaly", 
                "region": "North East Atlantic"
            }, 
            "Pc": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Phytoplankton", 
                "region": "North East Atlantic"
            }, 
            "S": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biodiversity", 
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Salinity", 
                "region": "North East Atlantic"
            }, 
            "T": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biodiversity", 
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Temperature", 
                "region": "North East Atlantic"
            }, 
            "Zc": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Zooplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Zooplankton", 
                "region": "North East Atlantic"
            }, 
            "euphDepth": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biodiversity", 
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Euphotic depth", 
                "region": "North East Atlantic"
            }, 
            "netPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Primary Production", 
                "region": "North East Atlantic"
            }, 
            "pCO2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
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
                "interval": "Monthly", 
                "niceName": "Ammonia", 
                "region": "Mediterranean Sea"
            }, 
            "NPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Primary Production", 
                "region": "Mediterranean Sea"
            }, 
            "Nitrate": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Nitrate", 
                "region": "Mediterranean Sea"
            }, 
            "Oxygen": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "interval": "Monthly", 
                "niceName": "Oxygen", 
                "region": "Mediterranean Sea"
            }, 
            "Phosphate": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Phosphate", 
                "region": "Mediterranean Sea"
            }, 
            "R_NO3_PHOS": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "interval": "Monthly", 
                "niceName": "Nitrate/Phosphate ratio", 
                "region": "Mediterranean Sea"
            }, 
            "R_NO3_SIO4": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "interval": "Monthly", 
                "niceName": "Nitrate/Silicate ratio", 
                "region": "Mediterranean Sea"
            }, 
            "Silicate": {
                "Confidence": "High", 
                "Ecosystem_Element": "Nutrient", 
                "interval": "Monthly", 
                "niceName": "Silicate", 
                "region": "Mediterranean Sea"
            }, 
            "Totchl": {
                "Confidence": "High", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Chlorophyll", 
                "region": "Mediterranean Sea"
            }, 
            "TotphytoC": {
                "Confidence": "High", 
                "Ecosystem_Element": "Phytoplankton", 
                "interval": "Monthly", 
                "niceName": "Phytoplankton", 
                "region": "Mediterranean Sea"
            }, 
            "Totzoo": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Zooplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Foodwebs", 
                    "Fisheries"
                ], 
                "interval": "Monthly", 
                "niceName": "Zooplankton", 
                "region": "Mediterranean Sea"
            }, 
            "pCO2": {
                "Confidence": "High", 
                "Ecosystem_Element": "Gases", 
                "interval": "Monthly", 
                "niceName": "pCO2", 
                "region": "Mediterranean Sea"
            }, 
            "sal": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Salinity", 
                "region": "Mediterranean Sea"
            }, 
            "temp": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrography"
                ], 
                "interval": "Monthly", 
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
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Chlorophyll", 
                "region": "Black Sea"
            }, 
            "MLD": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Mixed Layer Depth", 
                "region": "Black Sea"
            }, 
            "NO3": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity"
                ], 
                "interval": "Monthly", 
                "niceName": "Nitrate", 
                "region": "Black Sea"
            }, 
            "NPP": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Phytoplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Primary Production", 
                "region": "Black Sea"
            }, 
            "O2": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "Oxygen", 
                "region": "Black Sea"
            }, 
            "PO4": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Nutrient", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity"
                ], 
                "interval": "Monthly", 
                "niceName": "Phosphate", 
                "region": "Black Sea"
            }, 
            "S": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biodiversity", 
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Salinity", 
                "region": "Black Sea"
            }, 
            "T": {
                "Confidence": "High", 
                "Ecosystem_Element": "Physics", 
                "MSFD": [
                    "Biodiversity", 
                    "Hydrography"
                ], 
                "interval": "Monthly", 
                "niceName": "Temperature", 
                "region": "Black Sea"
            }, 
            "Z": {
                "Confidence": "Low", 
                "Ecosystem_Element": "Zooplankton", 
                "MSFD": [
                    "Eutrophication", 
                    "Biodiversity", 
                    "Foodwebs"
                ], 
                "interval": "Monthly", 
                "niceName": "Zooplankton", 
                "region": "Black Sea"
            }, 
            "pCO2w": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Gases", 
                "MSFD": [
                    "Eutrophication"
                ], 
                "interval": "Monthly", 
                "niceName": "pCO2", 
                "region": "Black Sea"
            }
        }, 
        "name": "metu_monthly", 
        "options": {
            "positive": "down", 
            "providerShortTag": "IMSMETU"
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
            "anchovy": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Fish", 
                "interval": "Monthly", 
                "niceName": "Anchovy", 
                "region": "Mediterranean Sea"
            }, 
            "sardine": {
                "Confidence": "Medium", 
                "Ecosystem_Element": "Fish", 
                "interval": "Monthly", 
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
    }
]
