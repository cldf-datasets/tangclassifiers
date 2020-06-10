from pycldf import StructureDataset, Source, Sources
from csvw.dsv import UnicodeDictReader
from pathlib import Path
from clldutils.misc import slug
from collections import defaultdict

# set up raw data path (globally)
raw_data = Path(__file__).parent.joinpath('raw')

# define parameters on the fly
parametertable = [
        {
            'ID': 'sortalclassifier', 'Name': 'sortal classifier', 'Description':
            'Does the language have sortal classifiers, regardless of optional of obligatory.'
            },
        {
            'ID': 'morphosyntacticplural', 'Name': 'morphosyntactic plural', 'Description':
            'Does the language have morphosyntactic plural markers.'
            }]

# add sources
sources = Sources.from_file(raw_data.joinpath('sources.bib'))
l2s = defaultdict(list)
active_sources = []
for src in sources.items():
    if src.get('Wals_code'):
        l2s[src['Wals_code']] += [src.id]
        active_sources += [src]


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
            "Source": l2s.get(row['wals_code'], [])
            }]
        formtable += [{
            "ID": '{0}-{1}-{2}'.format(lidx, 'morphosyntacticplural', i),
            "Value": row['morphosyntactic_plural'],
            "Language_ID": lidx,
            "Parameter_ID": 'morphosyntacticplural',
            "Source": l2s.get(row['wals_code'], [])
            }]

# we access our dataset that will be created now
ds = StructureDataset.in_dir('cldf')

# we add sources here manually, they will be rendered in bibtex
ds.add_sources(
        *active_sources
        )

ds.add_component('ParameterTable')
ds.add_component('LanguageTable')
ds.write(ValueTable=formtable, ParameterTable=parametertable,
        LanguageTable=languagetable)

ds.write_metadata()
ds.write_sources()
