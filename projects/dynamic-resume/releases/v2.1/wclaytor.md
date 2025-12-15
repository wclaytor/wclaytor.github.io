# wclaytor notes

This version is much closer. There are a few more issues:

In the navigation section, 'Home' is a separate button. Insetead, it should be the first option in the list of sections, like:

- Home
- Links
- etc...

Speaking of the section navigation, we do not need a label to tell us what the section contains ('text'). Please remove these.

The 'Short' button is not explanatory. In the same way that we have 'Theme: Dark' we should have 'Content: Short'.

The links should be removed from the William Claytor header as they are also in the Links section.

The Links section should just be one of the sections, not a heading section with a surround like William Claytor. There is already a leftover Links section heading and this is where the links should go. And when we do display the links, we should have a label and then the URL of the link as the link. This way when it is printed the URLs are displayed rather than just the text 'Personal website', etc... And this way users can see the URL they are about to visit to ensure it is valid and safe.

And lastly, please also tweak the header to include that “US citizen willing to relocate…” line (right now it isn’t captured by the minimal parser, since it’s a pre-section bullet). That’s easy to support by adding a headerBullets field in the parsed model.