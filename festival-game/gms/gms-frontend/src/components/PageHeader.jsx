import React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@material-ui/core/AppBar';
import styled, { css } from 'styled-components';
import { Badge, IconButton, Toolbar, Typography } from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';
import NotificationsIcon from '@material-ui/icons/Notifications';

const PageHeader = ({ open, onOpen, drawerWidth, children }) => {
  return (
    <HeaderBlock position="absolute" $open={open} $drawerWidth={drawerWidth}>
      <Toolbar>
        <MenuButton
          edge="start"
          color="inherit"
          aria-label="open drawer"
          onClick={onOpen}
          $hidden={open}
        >
          <MenuIcon />
        </MenuButton>
        <HeaderTitle component="h1" variant="h6" color="inherit" noWrap>
          {children}
        </HeaderTitle>
        <IconButton color="inherit">
          <Badge badgeContent={4} color="secondary">
            <NotificationsIcon />
          </Badge>
        </IconButton>
      </Toolbar>
    </HeaderBlock>
  );
};

PageHeader.propTypes = {
  open: PropTypes.bool,
  onOpen: PropTypes.func,
  drawerWidth: PropTypes.number,
  children: PropTypes.string,
};

PageHeader.defaultProps = {
  open: true,
  onOpen: null,
  drawerWidth: 0,
  children: 'Application',
};

const HeaderBlock = styled(AppBar)`
  z-index: ${({ theme }) => theme.zIndex.drawer + 1};
  transition: ${({ theme }) =>
    theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    })};
  ${props =>
    props.$open &&
    css`
      margin-left: ${props.$drawerWidth}px;
      width: calc(100% - ${props.$drawerWidth}px);
      transition: ${({ theme }) =>
        theme.transitions.create(['width', 'margin'], {
          easing: theme.transitions.easing.sharp,
          duration: theme.transitions.duration.enteringScreen,
        })};
    `}
`;

const MenuButton = styled(IconButton)`
  margin-right: 36px;
  display: ${props => (props.$hidden ? 'none' : 'block')};
`;

const HeaderTitle = styled(Typography)`
  flex-grow: 1;
`;

export default PageHeader;
