# Next Steps

Now you have a working foundation for a more accessible website! What should you do next? Here are a few things you can do with your starter project.

## Customize other key models.

As we said earlier in the tutorial, custom models are pretty important to take care of early in a project. This project already comes with a custom image model but you'll want to customize the user and document models as well just in case you need to use them later on in your project. Here are links to the documentation on how to customize each model, including a link on how to customize the image and renditon models from scratch:

- [User](https://docs.wagtail.org/en/stable/advanced_topics/customisation/custom_user_models.html#custom-user-models)
- [AbstractImage and AbstractRendition](https://docs.wagtail.org/en/stable/advanced_topics/images/custom_image_model.html#custom-image-model)
- [AbstractDocument](https://docs.wagtail.org/en/stable/advanced_topics/documents/custom_document_model.html#id1)

## Add your favorite frontend

Wagtail was created to provide a backend framework that works well with as many frontend technologies as possible. Whether you prefer something simple like [Bootstrap](https://getbootstrap.com/) or something more complex like [React](https://reactjs.org/) or [Next.js](https://nextjs.org/), you can try pretty much everything with Wagtail. If you need some inspiration, see the [Awesome Wagtail repository](https://github.com/springload/awesome-wagtail) for some good starter templates and other resources.

## Install some packages

Content people have high expectations, and the default options in Wagtail don't typically satisfy them. So try adding some packages to expand Wagtail and add some key functions like SEO support and other useful features. Have a look at our [Packages directory](https://wagtail.org/packages/) to see which ones might be useful for your project. You can also find great packages at [Django Packages](https://djangopackages.org/) as well. 

## Experiment with adding different elements from the Wagtail Extended Tutorial

The [Wagtail Extended Tutorial](https://docs.wagtail.org/en/stable/tutorial/index.html) includes an example project that can provide you with some code examples to borrow for your own work. Have a look at it and see if there are any bits you like and want to try out.

## Deploy your project

There are so many options for deployment, we can't cover them all. But the [Wagtail Extended Tutorial](https://docs.wagtail.org/en/stable/tutorial/index.html) contains deployment instructions and you can also find some [deployment resources in the Wagtail documentation](https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#deployment-guide).

## Experiment with StreamField blocks

There is a whole list of [default blocks](https://docs.wagtail.org/en/stable/reference/streamfield/blocks.html) you can use in Wagtail. You can also combine these blocks in custom arrangements with [StructBlock](https://docs.wagtail.org/en/stable/topics/streamfield.html#structblock). If the default blocks aren't quite what you need, you can even add [custom blocks](https://docs.wagtail.org/en/stable/advanced_topics/customisation/streamfield_blocks.html#custom-streamfield-blocks) to your project. StreamField goes about as far as your imagination goes!

For more on custom validation in Wagtail, [check out the video of Scott's talk](https://www.youtube.com/watch?v=UVBHciwpgKM) from Wagtail Space US in June.

## Run some accessibility tests

### Single page in-browser testing

- [Axe DevTools](https://www.deque.com/get-started-axe-devtools-browser-extension/)
- [Accessibility Insights (Chrome/Edge only)](https://accessibilityinsights.io/)
- [IBM Equal Access Accessibility Checker](https://www.ibm.com/able/toolkit/verify/automated)
- [WAVE](https://wave.webaim.org/)
- [Sa11y](https://sa11y.netlify.app/)
- [wagtail-accessibility](https://github.com/wagtail-nest/wagtail-accessibility) (tota11y integration)

### Bulk testing tools and services

- [Pa11y](https://pa11y.org/)
- [Storybook](https://storybook.js.org/docs/writing-tests/accessibility-testing)
- [BrowserStack](https://www.browserstack.com/accessibility-testing)

### Manual testing

- Keyboard navigation
- Screen readers ([see usage data](https://webaim.org/projects/screenreadersurvey10/))
  - macOS: VoiceOver with Safari
  - Windows: NVDA with Chrome
    - or JAWS, if you can pay for it
- Speech input
- OS native options (or Dragon, if you can pay for it)
- Further reading: [Designing and Coding for Voice](https://www.briandeconinck.com/designing-coding-voice/) by Brian DeConinck

## Do an accessibility audit

- Set up a spreadsheet, GitHub project, or some other tool to track your findings
- Start with your most popular/important pages
- Run them through each automated testing tool
  - Verify which findings are legitimate
  - Record them with two key metrics (up to your interpretation): severity and estimated effort to fix
- Do the same for manual testing processes
- Prioritize fixes based on impact/effort
- Consider trying [the Consumer Financial Protection Bureau’s guided audit tool](https://cfpb.github.io/design-system/guidelines/accessibility-audit-tools#cfpb-manual-web-accessibility-audit)

## Further reading on accessibility

- Wagtail docs: [Accessibility Considerations](https://docs.wagtail.org/en/stable/advanced_topics/accessibility_considerations.html)
- [WebAIM](https://webaim.org/)
- [The A11Y Project](https://www.a11yproject.com/)
- [TPGi’s technical blog](https://www.tpgi.com/technical/)
- [Inclusive Components](https://inclusive-components.design/)
- The [Accessibility Weekly](https://a11yweekly.com/) newsletter

## And a final list of key resources for learning Wagtail

- [wagtail.org](https://wagtail.org/), the project homepage
- The Wagtail Bakery Demo: https://github.com/wagtail/bakerydemo
- Wagtail Docs: https://docs.wagtail.org/
- Wagtail User Guide: https://guide.wagtail.org/
- [Wagtail Getting Started Tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)
- [Learn Wagtail](https://learnwagtail.com/), an amazing collection of tutorials and courses
