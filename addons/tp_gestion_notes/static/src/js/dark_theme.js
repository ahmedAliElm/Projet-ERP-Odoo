/** @odoo-module **/

import { Component, onMounted, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

/**
 * Dark Theme Manager for TP Gestion Notes
 * Provides a floating toggle button to switch between light and dark themes
 * Theme preference is stored in localStorage for persistence
 */
class DarkThemeService {
    constructor() {
        this.setup();
    }

    setup() {
        // Apply saved theme on page load
        this.applyDarkTheme();
        // Setup the floating toggle button
        this.setupThemeToggle();
    }

    applyDarkTheme() {
        // Check localStorage for theme preference
        const localStorageTheme = localStorage.getItem('tp_notes_dark_theme');

        if (localStorageTheme !== null) {
            const isDark = localStorageTheme === 'true';
            this.toggleDarkTheme(isDark);
        }

        // Add container class for custom styling
        document.body.classList.add('tp_note_container');
    }

    toggleDarkTheme(enable) {
        const body = document.body;
        const webClient = document.querySelector('.o_web_client');

        if (enable) {
            body.classList.add('o_dark_mode', 'tp_note_dark');
            if (webClient) {
                webClient.classList.add('o_dark_mode');
            }
        } else {
            body.classList.remove('o_dark_mode', 'tp_note_dark');
            if (webClient) {
                webClient.classList.remove('o_dark_mode');
            }
        }
    }

    setupThemeToggle() {
        // Check if button already exists
        if (document.querySelector('.tp_theme_toggle')) {
            return;
        }

        // Create the toggle button (transparent, no border)
        const toggleButton = document.createElement('button');
        toggleButton.className = 'tp_theme_toggle';
        toggleButton.title = 'Basculer thème sombre/clair';
        // Transparent background, no border, large icon
        toggleButton.style.cssText = 'position: fixed; bottom: 20px; right: 20px; z-index: 1000; background: transparent !important; background-image: none !important; box-shadow: none !important; border: none !important; outline: none !important; cursor: pointer; padding: 0; transition: transform 0.3s ease;';

        // Add hover effect
        toggleButton.onmouseover = () => toggleButton.style.transform = 'scale(1.1)';
        toggleButton.onmouseout = () => toggleButton.style.transform = 'scale(1)';

        // Set initial icon based on current theme
        const isDark = document.body.classList.contains('o_dark_mode');
        if (isDark) {
            // In Dark Mode, show Sun (Yellow/Orange)
            toggleButton.innerHTML = '<i class="fa fa-sun-o" style="font-size: 40px; color: #f39c12; text-shadow: 0 0 10px rgba(243, 156, 18, 0.5);"></i>';
        } else {
            // In Light Mode, show Moon (Dark Blue/Gray)
            toggleButton.innerHTML = '<i class="fa fa-moon-o" style="font-size: 40px; color: #34495e;"></i>';
        }

        // Add click handler
        toggleButton.addEventListener('click', () => {
            const currentlyDark = document.body.classList.contains('o_dark_mode');
            this.toggleDarkTheme(!currentlyDark);

            // Save preference
            localStorage.setItem('tp_notes_dark_theme', (!currentlyDark).toString());

            // Update icon
            if (!currentlyDark) {
                // Switching TO Dark Mode -> Show Sun
                toggleButton.innerHTML = '<i class="fa fa-sun-o" style="font-size: 40px; color: #f39c12; text-shadow: 0 0 10px rgba(243, 156, 18, 0.5);"></i>';
            } else {
                // Switching TO Light Mode -> Show Moon
                toggleButton.innerHTML = '<i class="fa fa-moon-o" style="font-size: 40px; color: #34495e;"></i>';
            }
        });

        // Add to body
        document.body.appendChild(toggleButton);
    }
}

// Initialize the dark theme service when the web client starts
registry.category("services").add("tp_dark_theme", {
    start() {
        return new DarkThemeService();
    },
});

export default DarkThemeService;

