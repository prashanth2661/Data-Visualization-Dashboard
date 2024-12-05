# Data-Visualization-Dashboard
Data visualization dashboard built using Flask for backend handling and Dash for interactive data visualizations. The primary goal of this dashboard is to present the Electric Vehicle Population Data in a visually appealing and easily digestible manner.

### Key Components

1. **Data Source**:
   - **File**: `Electric_Vehicle_Population_Data.csv`
   - **Columns**:
     - VIN (1-10)
     - County
     - City
     - State
     - Postal Code
     - Model Year
     - Make
     - Model
     - Electric Vehicle Type
     - Clean Alternative Fuel Vehicle (CAFV) Eligibility
     - Electric Range
     - Base MSRP
     - Legislative District
     - DOL Vehicle ID
     - Vehicle Location
     - Electric Utility
     - 2020 Census Tract

2. **Backend Framework**:
   - **Flask**: A lightweight WSGI web application framework in Python that provides the structure for routing requests and rendering templates.

3. **Interactive Dashboard**:
   - **Dash**: A productive Python framework for building web applications, designed for creating complex, custom data visualizations. It seamlessly integrates with Flask.
   - **Graph Types**:
     - **Bar Chart**: Displays the distribution of electric utilities across cities.
     - **Line Chart**: Shows trends over cities and makes.
     - **Scatter Plot**: Visualizes the relationship between base MSRP and city, categorized by electric vehicle type.

4. **Project Structure**:
   - **app.py**: The main application file, where Flask and Dash are configured and executed.
   - **templates/index.html**: The HTML template rendered by Flask, embedding the Dash app within an iframe.
   - **static/style.css**: Optional CSS for styling the HTML template.

### Functional Flow

1. **Initialization**:
   - The Flask app is initialized first to handle the main routing and HTML rendering.
   - Dash is set up to create interactive visualizations, and its server is linked with Flask.

2. **Data Loading**:
   - The CSV file is loaded into a Pandas DataFrame, enabling easy manipulation and visualization.

3. **Dash Layout**:
   - The layout of the Dash app consists of several `dcc.Graph` components, each linked to a specific plotly express figure.

4. **Rendering and Serving**:
   - The main Flask route (`/`) serves the `index.html` template.
   - The template includes an iframe that embeds the Dash app, enabling seamless integration between Flask and Dash.

### Usage
1. **Running the Application**:
   - Execute `app.py` to start the server.
   - Navigate to `http://127.0.0.1:5000/` in a web browser to view and interact with the dashboard.

2. **Viewing Data**:
   - The dashboard provides intuitive visualizations that help in understanding the distribution, trends, and relationships within the Electric Vehicle Population Data.

### Additional Features
- **Interactivity**: The Dash app offers interactive features like hovering over data points to get more information, zooming into graphs, and filtering data in real-time.
- **Customization**: Users can easily modify the plots and layout by altering the Dash app layout and graph configurations in `app.py`.

This dashboard is an excellent tool for visualizing complex data sets and making data-driven decisions.

**For queries reach out to my LinkedIn profile**
