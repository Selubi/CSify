import spacy
import deepl


class Csify:
    def __init__(self, en_dependency_parser, jp_dependency_parser, translator):
        self.en_dependency_parser = en_dependency_parser
        self.jp_dependency_parser = jp_dependency_parser
        self.translator = translator

    def en_to_cs(self, to_translate):
        return en_to_cs(to_translate, self.en_dependency_parser, self.translator)

    def ja_to_cs(self, to_translate):
        return ja_to_cs(to_translate, self.jp_dependency_parser, self.translator)


def en_to_cs(en_text, en_dependency_parser, translator):
    """Generates EN based code switched sentence.
    Converts the largest (longest) subtree among Dependency Tree ROOT's first child and then translates it.
    If the first word is SCONJ, exclude it from the translation.
    Translates in place (no position change for phrases)"""
    tokenized = en_dependency_parser(en_text)  # Runs spacy parser.
    result = ""

    for token in tokenized:

        if token.dep_ == "ROOT":
            root_pos = len(list(token.lefts))

            to_translate, largest_subtree_index, largest_subtree_root = get_largest_subtree(
                token.children)

            i = -1
            for root in token.children:  # Iterates through first children
                i += 1
                # Adds the current root to its position
                if i == root_pos:
                    result += token.text + ' '
                # Translates and adds the largest subtree
                if i == largest_subtree_index and to_translate:
                    result += \
                        translator.translate_text(
                            to_translate, target_lang="JA").text + ' '
                    continue
                # Adds the remaining subtree
                result += flatten_tree(root) + ' '
            # Adds the root if the root is on mostright
            if root_pos > i:
                result += token.text

            # # for debugging
            # print([list(i.subtree) for i in token.children])
            # print(to_translate)
            # print(token.text)

    return result


def ja_to_cs(en_text, jp_dependency_parser, translator):
    """Generates JP based code switched sentence.
    Converts the largest (longest) subtree among Dependency Tree ROOT's left first child and then translates it.
    If the last character is a japanese particle exclude it from the translation.
    Translates in place (no position change for phrases)"""
    tokenized = jp_dependency_parser(en_text)  # Runs spacy parser.
    result = ""

    for token in tokenized:

        if token.dep_ == "ROOT":
            root_pos = len(list(token.lefts))

            to_translate, largest_subtree_index, largest_subtree_root = get_largest_subtree(
                token.lefts)
            i = -1
            for root in token.children:  # Iterates through first children
                i += 1
                # Adds the current root to its position
                if i == root_pos:
                    result += token.text
                # Translates and adds the largest subtree
                if i == largest_subtree_index and to_translate:
                    result += translator.translate_text(
                        to_translate, target_lang="EN-US").text.strip('.?!')
                    continue
                # Adds the remaining subtree
                result += flatten_tree(root)
            # Adds the root if the root is on mostright
            if root_pos > i:
                result += token.text

            # # for debugging
            # print([list(i.subtree) for i in token.children])
            # print(to_translate)
            # print(token.text)

    return result


def flatten_tree(tree):
    """Returns concatenated string of a spacy subtree given tree root."""
    return ''.join([token.text_with_ws for token in list(tree.subtree)]).strip()


def get_largest_subtree(forest):
    """
    Given a list of tree roots, Returns flattened string of tree_root's largest child subtree and its index.
    If the child subtree only has size of one, only add it if it is a NOUN.
    """
    largest_subtree_index = -1
    flattened_largest_subtree = ""
    largest_subtree_size = 0
    largest_subtree_root = None
    i = -1
    for child_root in forest:
        i += 1
        subtree_length = len(list(child_root.subtree))

        if subtree_length > largest_subtree_size:
            if subtree_length == 1:
                if child_root.pos_ != 'NOUN':
                    continue

            # Update new largest subtree
            largest_subtree_size = subtree_length
            largest_subtree_index = i
            largest_subtree_root = child_root
            flattened_largest_subtree = flatten_tree(child_root)

    return flattened_largest_subtree, largest_subtree_index, largest_subtree_root