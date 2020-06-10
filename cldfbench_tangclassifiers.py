import pathlib
import collections

from pycldf import Sources
from cldfbench import Dataset as BaseDataset, CLDFSpec
from clldutils.misc import slug


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "tangclassifiers"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(dir=self.cldf_dir, module='StructureDataset')

    def cmd_download(self, args):
        pass

    def cmd_makecldf(self, args):
        args.writer.cldf.add_component('ParameterTable')
        args.writer.cldf.add_component(
            'LanguageTable',
            'Continent', 'Genus', 'WALSCode',  # we add more language metadata
        )

        args.writer.objects['ParameterTable'] = [
        {
            'ID': 'sortalclassifier',
            'Name': 'sortal classifier',
            'Description':
            'Does the language have sortal classifiers, regardless of optional of obligatory.'
        },
        {
            'ID': 'morphosyntacticplural',
            'Name': 'morphosyntactic plural',
            'Description':
            'Does the language have morphosyntactic plural markers.'
        }]

        l2s = collections.defaultdict(list)
        sources = []
        for src in sorted(
                Sources.from_file(self.raw_dir / 'sources.bib').items(), key=lambda i: i.id):
            if src.get('Wals_code'):
                l2s[src['Wals_code']].append(src.id)
                sources += [src]

        args.writer.cldf.add_sources(*sources)

        for row in self.raw_dir.read_csv('GSSG_ListOfLanguages.csv', delimiter=';', dicts=True):
            lidx = slug(row['language_name'], lowercase=False)
            args.writer.objects['LanguageTable'].append({
                'ID': lidx,
                'Name': row['language_name'],
                'Latitude': row['latitude'],
                'Longitude': row['longitude'],
                'Glottocode': row['glottocode'],
                'ISO639P3code': row['iso_code'],
                'Continent': row['continent'],
                'Genus': row['genus'],
                'WALSCode': row['wals_code']
            })
            for param in ['sortal_classifier', 'morphosyntactic_plural']:
                pid = param.replace('_', '')
                args.writer.objects['ValueTable'].append({
                    "ID": '{0}-{1}'.format(lidx, pid),
                    "Value": row['sortal_classifier'],
                    "Language_ID": lidx,
                    "Parameter_ID": pid,
                    "Source": l2s.get(row['wals_code'], [])
                })
