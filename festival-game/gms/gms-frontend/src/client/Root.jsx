import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import App from 'shared/App';
import GlobalStyle from 'GlobalStyle';
import { ThemeProvider } from 'styled-components';
import { MuiThemeProvider, StylesProvider } from '@material-ui/core';
import { createMuiTheme } from '@material-ui/core/styles';

const Root = () => {
  const theme = createMuiTheme({
    palette: {
      primary: {
        main: '#222831',
      },
    },
  });

  return (
    <StylesProvider injectFirst>
      <MuiThemeProvider theme={theme}>
        <ThemeProvider theme={theme}>
          <BrowserRouter>
            <GlobalStyle />
            <App />
          </BrowserRouter>
        </ThemeProvider>
      </MuiThemeProvider>
    </StylesProvider>
  );
};

export default Root;
