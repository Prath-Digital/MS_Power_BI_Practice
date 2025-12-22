# Power BI Bookmarks, Navigation, Slicers, and Parameters FAQ

## Q.1 What is a bookmark in Power BI and what is its primary use?

A bookmark in Power BI captures the current state of a report page, including applied filters, slicers, visual states (like visibility, spotlight, and sort order), cross-highlighting, and more.  

Its primary use is to save specific views of a report page for quick navigation, creating guided storytelling experiences, interactive presentations, or personalized views that users can return to easily.

## Q.2 How can bookmarks be used to create interactive reports or narratives?

Bookmarks enable interactivity by allowing users to step through predefined views (e.g., sequenced insights for storytelling). They can be linked to buttons or shapes for custom navigation, toggling visuals, hiding/showing elements, or presenting data in a narrative flow, turning static reports into dynamic, app-like experiences.

## Q.3 What are the differences between data, display, and current page options when saving a bookmark?

- **Data**: Captures filters, slicers, and other data-related states (e.g., selections that affect what data is shown).
- **Display**: Captures visual properties like visibility, spotlight, and zoom (but not data filters).
- **Current page**: Switches to the page where the bookmark was created when selected (useful for navigation across pages).  

By default, all are enabled; unchecking them allows selective control (e.g., change visibility without resetting filters).

## Q.4 How do you create a custom navigation button in Power BI?

Insert a button (Insert > Buttons > Blank or predefined), or use shapes/images. Customize its appearance (fill, icon, text). In the Format pane, turn on Action, select "Bookmark" or "Page navigation" as the type, and link to a bookmark or target page for navigation.

## Q.5 What are some common actions you can assign to a navigation button using bookmarks?

- Navigate to a specific page or view.
- Toggle visibility of visuals or slicer panels.
- Reset filters/slicers.
- Spotlight a visual.
- Switch between chart types or scenarios.
- Clear selections or show/hide elements for interactive toggles.

## Q.6 How can custom buttons improve user experience in Power BI reports?

Custom buttons make reports feel like apps: intuitive navigation, guided storytelling, interactive toggles (e.g., show/hide details), and dynamic views. They reduce clutter, provide clear calls-to-action, and enhance engagement without overwhelming users with complex filters.

## Q.7 What is a slicer panel in Power BI and why is it used?

A slicer panel is a collapsible area (often a rectangle shape) containing multiple slicers, toggled via buttons and bookmarks. It is used to save canvas space, reduce clutter, and provide on-demand filtering while keeping the main report visuals prominent.

## Q.8 How do you create a collapsible slicer panel using bookmarks and shapes?

1. Add slicers and group them with a background rectangle shape.
2. Use the Selection pane to hide/show the group.
3. Create two bookmarks: one with the panel visible (Display enabled, Data disabled to avoid resetting filters), one hidden.
4. Add toggle buttons/shapes linked to these bookmarks via Action > Bookmark.

## Q.9 What are the advantages of using a slicer panel instead of placing all slicers directly on the report canvas?

- Saves valuable canvas space for key visuals.
- Reduces visual clutter for a cleaner, more focused report.
- Improves performance on dense reports.
- Provides on-demand access to filters, enhancing user experience without permanent obstruction.

## Q.10 What are numeric range parameters in Power BI and how are they configured?

Numeric range parameters (formerly "What-If" parameters) create dynamic variables for scenarios like discounts or growth rates.  

Configure via Modeling > New Parameter > Numeric range: set name, data type, minimum, maximum, increment, and default. Power BI auto-creates a table, measure, and optional slicer.

## Q.11 How can numeric range parameters be used to control dynamic filtering in visuals?

Use the parameter in DAX measures (e.g., projected sales = sales * (1 + parameter value)). Add the parameter as a slicer; adjusting it dynamically recalculates and filters visuals (e.g., threshold-based highlighting or what-if analysis).

## Q.12 What is the difference between a numeric slicer and a parameter-based numeric filter?

- **Numeric slicer**: A visual on-canvas filter using a field/column for range selection (e.g., filter sales between values); directly filters underlying data rows.
- **Parameter-based numeric filter**: A dynamic variable (not tied to data) for what-if scenarios; used in measures for calculations (e.g., simulated growth), not direct row filtering. It's interactive via slicer but affects computations, not raw data rows.