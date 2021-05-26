import React from 'react';
import PropTypes from 'prop-types';
import styled, { css } from 'styled-components';
import Drawer from '@material-ui/core/Drawer';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';

const PageNavigation = ({ open, onClose }) => {
  return (
    <NavigationBlock variant="permanent" $open={open}>
      <ToolbarIcon>
        <IconButton onClick={onClose}>
          <ChevronLeftIcon />
        </IconButton>
      </ToolbarIcon>
      <Divider />
    </NavigationBlock>
  );
};

PageNavigation.propTypes = {
  open: PropTypes.bool,
  onClose: PropTypes.func,
};

PageNavigation.defaultProps = {
  open: true,
  onClose: null,
};

const NavigationBlock = styled(Drawer)`
  position: relative;
  white-space: nowrap;
  width: ${props => props.$drawWidth};
  transition: ${({ theme }) =>
    theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    })};
  ${props =>
    props.$hidden &&
    css`
      overflow-x: 'hidden';
      transition: ${props.theme.transitions.create('width', {
        easing: props.theme.transitions.easing.sharp,
        duration: props.theme.transitions.duration.leavingScreen,
      })};
      width: theme.spacing(7);
    `}
`;

const ToolbarIcon = styled.div`
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding: 0 8px;

  min-height: 56px;
  @media (min-width: 0px) and (orientation: landscape) {
    min-height: 48px;
  }
  @media (min-width: 600px) {
    min-height: 64px;
  }
`;

export default PageNavigation;
