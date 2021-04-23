module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  parser: "@typescript-eslint/parser",
  parserOptions: {
    sourceType: "module",
    ecmaVersion: 2021,
  },
  extends: [
    "plugin:react-hooks/recommended",
    "react-app",
    'airbnb',
    'prettier/react', // ? for airbnb
    'eslint:recommended',
  ],
  rules: {
    "react-hooks/exhaustive-deps": "off", // ? https://github.com/facebook/react/issues/14920#issuecomment-471070149
  },
  globals: {
    ActionTypes: true,
    Action: true,
  }
};