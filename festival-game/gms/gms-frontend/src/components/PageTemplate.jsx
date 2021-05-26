import React, { useState } from 'react';
import styled from 'styled-components';
import PageHeader from './PageHeader';
import PageNavigation from './PageNavigation';

const PageTemplate = () => {
  const [open, setOpen] = useState(false);

  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <PageTemplateBlock>
      <PageHeader open={open} onOpen={handleDrawerOpen} drawerWidth={240}>
        ESD-GMS
      </PageHeader>
      <PageNavigation open={open} onClose={handleDrawerClose} />
    </PageTemplateBlock>
  );
};

const PageTemplateBlock = styled.div`
  display: flex;
`;

export default PageTemplate;
