from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def test_load(repo_dir: "Path") -> None:
    from ontopy import get_ontology

    # Check that the defaults works
    emmo = get_ontology('emmo').load()  # ttl format
    assert emmo.Atom.prefLabel.first() == 'Atom'

    emmo = get_ontology('emmo-inferred').load()
    assert emmo.Atom.prefLabel.first() == 'Atom'

    emmo = get_ontology('emmo-development').load()  # ttl format
    assert emmo.Atom.prefLabel.first() == 'Atom'

    emmo = get_ontology('https://emmo-repo.github.io/latest-stable/'
                        'emmo-inferred.owl').load()  # owl format
    assert emmo.Atom.prefLabel.first() == 'Atom'

    # Load a local ontology with catalog
    testonto = repo_dir / "tests" / "testonto" / "testonto.ttl"
    onto = get_ontology(str(testonto)).load()
    assert onto.TestClass.prefLabel.first() == 'TestClass'

    # Use catalog file when downloading from web
    onto = get_ontology(
        'https://raw.githubusercontent.com/BIG-MAP/BattINFO/master/'
        'battinfo.ttl').load()
    assert onto.Electrolyte.prefLabel.first() == 'Electrolyte'

    # Test loading of non-EMMObased ontology
    rdf_onto = get_ontology(
        'https://www.w3.org/1999/02/22-rdf-syntax-ns.ttl').load(
            EMMObased=False)
    rdfs_onto = get_ontology(
        'https://www.w3.org/2000/01/rdf-schema.ttl').load(
            EMMObased=False)
