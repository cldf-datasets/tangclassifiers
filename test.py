
def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_sample(cldf_dataset, cldf_logger):
    # Abun are sortalclassifiers = yes and morphosyntacticplural = no
    for row in cldf_dataset['ValueTable']:
        if row['Language_ID'] == 'Abun':
            if row['Parameter_ID'] == 'sortalclassifiers':
                assert row['Value'] == 'yes'
            if row['Parameter_ID'] == 'morphosyntacticplural':
                assert row['Value'] == 'no'
