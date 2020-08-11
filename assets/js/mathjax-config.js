window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: false,
    packages: {'[+]': ['noerrors']},
    tags: 'ams'
  },
  loader: {
    load: ['[tex]/noerrors']
  }
};
