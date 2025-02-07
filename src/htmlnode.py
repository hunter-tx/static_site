class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'
        return string

    def __eq__(self, compare):
        if (
            self.tag == compare.tag and
            self.value == compare.value and
            self.children == compare.children and
            self.props == compare.props
        ):
            return True
        return False


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        html_content = ""
        skipped_children = []
        for child in self.children:
            try:
                # Append valid child HTML
                html_content += child.to_html()
            except ValueError:
                # Skip invalid children
                skipped_children.append(child)
        if not html_content:
            raise ValueError("No valid children to render")
        tag = f'<{self.tag}{self.props_to_html()}>{html_content}</{self.tag}>'
        return tag

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
