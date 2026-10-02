"""Run with python -m unittest discover -s Test/Localization -v."""
import collections
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]

class ChineseCatalogTests(unittest.TestCase):
    def setUp(self):
        self.root = ET.parse(ROOT / 'Form/i18n/PokeFinder_zh.ts').getroot()
    def test_all_active_messages_are_translated(self):
        missing = []
        for context in self.root.findall('context'):
            for message in context.findall('message'):
                translation = message.find('translation')
                if translation is not None and translation.get('type') in ('vanished', 'obsolete'):
                    continue
                if translation is None or translation.get('type') == 'unfinished' or not ''.join(translation.itertext()).strip():
                    missing.append((context.findtext('name'), message.findtext('source')))
        self.assertEqual(missing, [])
    def test_placeholders_are_preserved(self):
        pattern = r'%(?:L?\d+|n)'
        for message in self.root.findall('.//message'):
            translation = message.find('translation')
            if translation is None or translation.get('type') in ('vanished', 'obsolete'):
                continue
            source = collections.Counter(re.findall(pattern, message.findtext('source', '')))
            for target in translation.findall('numerusform') or [translation]:
                self.assertEqual(source, collections.Counter(re.findall(pattern, ''.join(target.itertext()))), message.findtext('source'))
    def test_new_tools_have_chinese_labels(self):
        messages = {(c.findtext('name'),m.findtext('source')):m.findtext('translation') for c in self.root.findall('context') for m in c.findall('message')}
        self.assertEqual(messages['AdjacentSeeds','Adjacent Seeds'], '邻近种子')
        self.assertEqual(messages['AdvanceFinder','Advance Finder'], '推进数查找器')
        self.assertEqual(messages['Phenomenon','Phenomenon'], '特殊现象')
    def test_language_choice_preserves_english_and_chinese(self):
        source = (ROOT/'Form/Util/Settings.cpp').read_text()
        self.assertIn('"zh"', source)
        self.assertIn('"en"', source)


class ResourceIntegrityTests(unittest.TestCase):
    def test_resource_row_counts_and_numeric_keys(self):
        root=ROOT/'Core/Resources/i18n'
        for en in (root/'en').glob('*.txt'):
            zh=root/'zh'/en.name.replace('_en.','_zh.')
            a=en.read_text(encoding='utf-8-sig').splitlines()
            b=zh.read_text(encoding='utf-8-sig').splitlines()
            self.assertEqual(len(a),len(b),en.name)
            for source,target in zip(a,b):
                if en.stem.split('_')[0] not in {'species','moves','abilities','natures','powers','games'} and re.match(r'^\d+,',source):
                    keys=2 if en.name.startswith('forms_') else 1
                    self.assertEqual(source.split(',')[:keys],target.split(',')[:keys],(en.name,source,target))
    def test_characteristic_generation_ids_are_preserved(self):
        import json
        root=ROOT/'Core/Resources/i18n'
        en=json.loads((root/'en/characteristic_en.json').read_text())
        zh=json.loads((root/'zh/characteristic_zh.json').read_text())
        self.assertEqual(len(en),len(zh))
        for a,b in zip(en,zh):self.assertEqual(sorted(g for v in a.values() for g in v),sorted(g for v in b.values() for g in v))

if __name__ == '__main__':
    unittest.main()
