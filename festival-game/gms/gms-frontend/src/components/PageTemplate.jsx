import React, { useState } from 'react';
import styled from 'styled-components';
import PageHeader from './PageHeader';

const PageTemplate = () => {
  const [open, setOpen] = useState(false);

  const handleDrawerOpen = () => {
    setOpen(true);
  };
  // const handleDrawerClose = () => {
  //   setOpen(false);
  // };

  return (
    <PageTemplateBlock>
      <PageHeader open={open} onOpen={handleDrawerOpen}>
        ESD-GMS
      </PageHeader>
    </PageTemplateBlock>
  );
};

const PageTemplateBlock = styled.div`
  display: flex;
`;

export default PageTemplate;
