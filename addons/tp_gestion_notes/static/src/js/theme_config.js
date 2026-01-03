/** @odoo-module **/

/**
 * Theme Configuration for TP Gestion Notes
 * Defines color schemes, constants, and utility functions for theme management
 */

// Dark theme color palette
export const DARK_THEME_COLORS = {
    primary: '#1a1d21',
    secondary: '#2d3136',
    tertiary: '#3d4249',
    accent: '#4a90e2',
    text: '#e4e6eb',
    textSecondary: '#b0b3b8',
    border: '#3e4147',
    hover: '#2a2d32',
    success: '#2ecc71',
    warning: '#f39c12',
    danger: '#e74c3c',
    info: '#3498db',
};

// Light theme color palette (default Odoo colors)
export const LIGHT_THEME_COLORS = {
    primary: '#ffffff',
    secondary: '#f8f9fa',
    tertiary: '#e9ecef',
    accent: '#007bff',
    text: '#212529',
    textSecondary: '#6c757d',
    border: '#dee2e6',
    hover: '#e9ecef',
    success: '#28a745',
    warning: '#ffc107',
    danger: '#dc3545',
    info: '#17a2b8',
};

// Theme configuration constants
export const THEME_CONFIG = {
    storageKey: 'tp_notes_dark_theme',
    transitionDuration: 300, // ms
    toggleButtonSize: 50, // px
    toggleButtonPosition: {
        bottom: '20px',
        right: '20px',
    },
};

/**
 * Get current theme preference
 * @returns {boolean} true if dark theme is enabled
 */
export function isDarkThemeEnabled() {
    const stored = localStorage.getItem(THEME_CONFIG.storageKey);
    return stored === 'true';
}

/**
 * Set theme preference
 * @param {boolean} isDark - true to enable dark theme
 */
export function setThemePreference(isDark) {
    localStorage.setItem(THEME_CONFIG.storageKey, isDark.toString());
}

/**
 * Get color value for current theme
 * @param {string} colorName - name of the color from theme palette
 * @returns {string} color value
 */
export function getThemeColor(colorName) {
    const isDark = isDarkThemeEnabled();
    const palette = isDark ? DARK_THEME_COLORS : LIGHT_THEME_COLORS;
    return palette[colorName] || palette.primary;
}

console.log('TP Gestion Notes - Theme configuration loaded');
