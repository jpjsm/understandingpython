-- Table: public.Distribution

-- DROP TABLE IF EXISTS public."Distribution";

CREATE TABLE IF NOT EXISTS public."Distribution"
(
    "taxonID" text COLLATE pg_catalog."default",
    "occurrenceStatus" text COLLATE pg_catalog."default",
    "locationID" text COLLATE pg_catalog."default",
    locality text COLLATE pg_catalog."default",
    "countryCode" text COLLATE pg_catalog."default",
    source text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Distribution"
    OWNER to dba;

-- Table: public.SpeciesProfile

-- DROP TABLE IF EXISTS public."SpeciesProfile";

CREATE TABLE IF NOT EXISTS public."SpeciesProfile"
(
    "taxonID" text COLLATE pg_catalog."default",
    "isExtinct" text COLLATE pg_catalog."default",
    "isMarine" text COLLATE pg_catalog."default",
    "isFreshwater" text COLLATE pg_catalog."default",
    "isTerrestrial" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."SpeciesProfile"
    OWNER to dba;

-- Table: public.Taxon

-- DROP TABLE IF EXISTS public."Taxon";

CREATE TABLE IF NOT EXISTS public."Taxon"
(
"taxonID" text COLLATE pg_catalog."default",
"parentNameUsageID" text COLLATE pg_catalog."default",
"acceptedNameUsageID" text COLLATE pg_catalog."default",
"originalNameUsageID" text COLLATE pg_catalog."default",
"scientificNameID" text COLLATE pg_catalog."default",
"datasetID" text COLLATE pg_catalog."default",
"taxonomicStatus" text COLLATE pg_catalog."default",
"taxonRank" text COLLATE pg_catalog."default",
"scientificName" text COLLATE pg_catalog."default",
"scientificNameAuthorship" text COLLATE pg_catalog."default",
"notho" text COLLATE pg_catalog."default",
"genericName" text COLLATE pg_catalog."default",
"infragenericEpithet" text COLLATE pg_catalog."default",
"specificEpithet" text COLLATE pg_catalog."default",
"infraspecificEpithet" text COLLATE pg_catalog."default",
"cultivarEpithet" text COLLATE pg_catalog."default",
"nameAccordingTo" text COLLATE pg_catalog."default",
"namePublishedIn" text COLLATE pg_catalog."default",
"nomenclaturalCode" text COLLATE pg_catalog."default",
"nomenclaturalStatus" text COLLATE pg_catalog."default",
"kingdom" text COLLATE pg_catalog."default",
"phylum" text COLLATE pg_catalog."default",
"class" text COLLATE pg_catalog."default",
"order" text COLLATE pg_catalog."default",
"superfamily" text COLLATE pg_catalog."default",
"family" text COLLATE pg_catalog."default",
"subfamily" text COLLATE pg_catalog."default",
"tribe" text COLLATE pg_catalog."default",
"taxonRemarks" text COLLATE pg_catalog."default",
"references" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Taxon"
    OWNER to dba;

-- Table: public.VernacularName

-- DROP TABLE IF EXISTS public."VernacularName";

-- 'language', 'vernacularName'

CREATE TABLE IF NOT EXISTS public."VernacularName"
(
    "taxonID" text COLLATE pg_catalog."default",
    "language" text COLLATE pg_catalog."default",
    "vernacularName" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."VernacularName"
    OWNER to dba;

COPY public."Distribution"
FROM '/sample-data/latest_dwca/Distribution.csv'
CSV HEADER;

COPY public."SpeciesProfile"
FROM '/sample-data/latest_dwca/SpeciesProfile.csv'
CSV HEADER;

COPY public."Taxon"
FROM '/sample-data/latest_dwca/Taxon.csv'
CSV HEADER;

COPY public."VernacularName"
FROM '/sample-data/latest_dwca/VernacularName.csv'
CSV HEADER;