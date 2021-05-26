import React from 'react';
import { Route } from 'react-router-dom';
import PageTemplate from 'components/PageTemplate';
import Home from 'pages/Home';

const App = () => {
  return (
    <PageTemplate>
      <Route exact path="/" component={Home} />
    </PageTemplate>
  );
};

export default App;
