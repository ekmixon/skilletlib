from skilletlib import SkilletLoader
from skilletlib.utils.testing_utils import setup_dir

setup_dir()

context = {}


def load_and_execute_skillet(skillet_path: str) -> dict:
    skillet_loader = SkilletLoader()
    skillet = skillet_loader.load_skillet_from_path(skillet_path)

    print('=' * 80)
    print(f'Executing {skillet.label}\n'.center(80))

    return skillet.execute(context)


def test_inline_template():
    skillet_path = '../example_skillets/template_inline_skillet/'
    output = load_and_execute_skillet(skillet_path)
    assert 'template' in output
    rendered_output = output.get('template', '')
    assert 'Variable is present.' in rendered_output


def test_template_skillet():
    skillet_path = '../example_skillets/template_skillet'
    output = load_and_execute_skillet(skillet_path)
    assert 'template' in output
    rendered_output = output.get('template', '')

    assert 'You variable value is: present.' in rendered_output


if __name__ == '__main__':
    test_inline_template()
    test_template_skillet()
