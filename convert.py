from pycldf import StructureDataset, Source
from csvw.dsv import UnicodeDictReader
from pathlib import Path
from clldutils.misc import slug

# set up raw data path (globally)
raw_data = Path(__file__).parent.joinpath('raw')

# define parameters on the fly
parametertable = [
        {
            'ID': 'sortalclassifier', 'Name': 'sortal classifier', 'Description':
            'Sortal classifer +++ add description.'
            },
        {
            'ID': 'morphosyntacticplural', 'Name': 'morphosyntactic plural', 'Description':
            '+++ add description.'
            }]

# fill tables with values
formtable, languagetable = [], []
with UnicodeDictReader(raw_data.joinpath('GSSG_ListOfLanguages.csv'),
        delimiter=';') as reader:
    for i, row in enumerate(reader):
        lidx = slug(row['language_name'], lowercase=False)
        languagetable += [{
            'ID': lidx,
            'Name': row['language_name'],
            'Latitude': row['latitude'],
            'Longitude': row['longitude'],
            'Glottocode': row['glottocode'],
            'ISO639P3code': row['iso_code'],
            'Continent': row['continent'],
            'Genus': row['genus'],
            'WALSCode': row['wals_code']
            }]
        formtable += [{
            "ID": '{0}-{1}-{2}'.format(lidx, 'sortalclassifier', i),
            "Value": row['sortal_classifier'],
            "Language_ID": lidx,
            "Parameter_ID": 'sortalclassifier',
            "Source": ''
            }]
        formtable += [{
            "ID": '{0}-{1}-{2}'.format(lidx, 'morphosyntacticplural', i),
            "Value": row['morphosyntactic_plural'],
            "Language_ID": lidx,
            "Parameter_ID": 'morphosyntacticplural',
            "Source": ''
            }]

# we access our dataset that will be created now
ds = StructureDataset.in_dir('cldf')

# we add sources here manually, they will be rendered in bibtex
ds.add_sources(
        Source('article', 'Dummy', 
            author='Tang, Marc',
            journal='+++',
            volume="+++",
            number="+++",
            pages='+++',
            year="2010",
            title='+++',
            doi='+++',
        ))

ds.add_component('ParameterTable')
ds.add_component('LanguageTable')
ds.write(ValueTable=formtable, ParameterTable=parametertable,
        LanguageTable=languagetable)

ds.write_metadata()
ds.write_sources()
