---
name: Neo-Retro Utility
colors:
  surface: '#f6fafe'
  surface-dim: '#d6dade'
  surface-bright: '#f6fafe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f4f8'
  surface-container: '#eaeef2'
  surface-container-high: '#e4e9ed'
  surface-container-highest: '#dfe3e7'
  on-surface: '#171c1f'
  on-surface-variant: '#424754'
  inverse-surface: '#2c3134'
  inverse-on-surface: '#edf1f5'
  outline: '#727785'
  outline-variant: '#c2c6d6'
  surface-tint: '#005ac2'
  primary: '#0058be'
  on-primary: '#ffffff'
  primary-container: '#2170e4'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#6b38d4'
  on-secondary: '#ffffff'
  secondary-container: '#8455ef'
  on-secondary-container: '#fffbff'
  tertiary: '#515c71'
  on-tertiary: '#ffffff'
  tertiary-container: '#6a758a'
  on-tertiary-container: '#fefcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#d8e3fb'
  tertiary-fixed-dim: '#bcc7de'
  on-tertiary-fixed: '#111c2d'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#f6fafe'
  on-background: '#171c1f'
  surface-variant: '#dfe3e7'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  h2:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-main:
    fontFamily: Manrope
    fontSize: 15px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.02em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 0.25rem
  sm: 0.5rem
  md: 1rem
  lg: 1.5rem
  xl: 2rem
  gutter: 1rem
  container-padding: 1.5rem
---

## Brand & Style

This design system establishes a "neo-retro" aesthetic tailored for a high-performance help desk environment. The personality is precise, technical, and dependable, blending the structured data-density of early computing with the fluid, accessible refinements of modern SaaS. 

The style draws from **Minimalism** and **Modern Corporate** movements, but injects a "technical soul" through specific typographic pairings and structured layouts. The goal is to evoke a sense of professional mastery—providing tools that feel like a high-end instrument rather than a toy. It prioritizes clarity and information density without the visual fatigue associated with older, border-heavy interfaces.

## Colors

The palette is anchored by **Deep Slate (#1E293B)** for text and structural elements, providing a grounded, high-contrast foundation. **Vibrant Blue (#3B82F6)** serves as the primary action color, driving the "modern" feel of the interface. **Soft Lavender (#8B5CF6)** is used sparingly for secondary highlights, such as ticket categories or specialized tags, adding a layer of sophisticated differentiation.

**Light Gray (#F1F5F9)** functions as the primary background surface, creating a "cool" temperature that reduces eye strain during long shifts. Actionable elements utilize the primary blue, while inactive or decorative structural lines lean into the neutral spectrum.

## Typography

This design system utilizes a dual-font strategy to balance human-centric communication with technical precision. 

**Manrope** is the primary typeface for all UI elements, headings, and body copy. Its balanced, modern proportions ensure readability in dense ticket descriptions. 

**Space Grotesk** is introduced as a subtle "technical" accent. It is used exclusively for data values—such as Ticket IDs, timestamps, and system logs—and for small, all-caps labels. This distinction helps users subconsciously categorize information: Manrope for "what people said" and Space Grotesk for "system data."

## Layout & Spacing

The layout follows a **fluid grid** model with a sidebar-heavy architecture common in administrative tools. A 12-column system is used for internal dashboards, with a 16px (1rem) gutter. 

Spacing follows a strict 4px base unit to maintain a "tight," professional feel. While whitespace is used to separate high-level sections, the data-rich areas (like ticket queues) utilize condensed vertical spacing to maximize the information visible above the fold.

## Elevation & Depth

To move away from "harsh" retro borders, this design system uses **Ambient Shadows** and **Tonal Layers** to create depth.

1.  **Level 0 (Background):** The neutral light gray (#F1F5F9).
2.  **Level 1 (Cards/Containers):** Pure white (#FFFFFF) surfaces with a very soft, diffused shadow (0px 4px 12px rgba(30, 41, 59, 0.05)).
3.  **Level 2 (Popovers/Modals):** Pure white with a more pronounced shadow and a 1px border in a slightly darker gray (#E2E8F0) to define edges against the background.

Avoid heavy black shadows; use the Deep Slate (#1E293B) at very low opacities (5-8%) to keep the "shadows" feeling clean and modern.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding removes the "aggression" of sharp 90-degree corners while maintaining a structured, modular grid. 

- **Buttons & Inputs:** Use the base `rounded` (4px).
- **Cards & Major Containers:** Use `rounded-lg` (8px).
- **Checkboxes:** Use a small 2px radius to maintain a technical, square-ish feel.
- **Search Bars:** Can utilize `rounded-xl` (12px) to signify they are global, persistent elements.

## Components

### Buttons
Primary buttons use the Vibrant Blue (#3B82F6) with white text. Secondary buttons use a "ghost" style with a Slate text color and a subtle 1px border that appears on hover.

### Inputs & Fields
Input fields use a white background with a 1px border in Slate-200. On focus, the border transitions to Vibrant Blue with a soft 2px blue "glow" (outer shadow). Use the monospaced font for input values that represent technical data (e.g., serial numbers).

### Chips & Tags
Tags are used for status (e.g., "Open," "Resolved") and categories. Status tags use a "light-fill" approach: a desaturated background version of the status color with high-contrast text. Use the monospaced font for tag labels.

### Lists & Queues
Ticket lists should avoid horizontal borders between every item. Instead, use a subtle hover state (background color change to #F8FAFC) to highlight the active row.

### Additional Components
- **Activity Feed:** A vertical timeline using the monospaced font for timestamps and Manrope for the event description.
- **Metric Tiles:** Large-format numbers using Space Grotesk for a "dashboard" look, paired with small Manrope labels.