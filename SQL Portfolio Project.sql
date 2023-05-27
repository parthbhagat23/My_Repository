Select *
From PortfolioProject..CovidDeaths
order by 3,4
Select *
From PortfolioProject..CovidVaccinations
order by 3,4


-- selecting data to be used for this project
Select Location, date, total_cases, new_cases, total_deaths, population
From PortfolioProject..CovidDeaths
Order by 1,2


-- Total cases vs total deaths
Select Location, date, total_cases, new_cases, total_deaths, (total_deaths/
total_cases)*100 AS DeathPercentage
From PortfolioProject..CovidDeaths
Where Location like '%Canada%'
Order by 1,2


-- Total Infected population by date
Select Location, date, total_cases, new_cases, total_deaths, (total_cases/
population)*100 AS InfectedPopuation
From PortfolioProject..CovidDeaths
--Where Location like '%Canada%'
Order by 1,2


--Countries with highest infection rate
Select Location, Population, MAX(total_cases) as HighestInfectionCount, MAX
((total_cases/population))*100 AS HighestInfectedPopuationPercentage
From PortfolioProject..CovidDeaths
Group by Location, Population
Order by HighestInfectedPopuationPercentage desc


--Countries with highest death count
Select Location, MAX(cast(total_deaths as int)) AS TotalDeathCount
From PortfolioProject..CovidDeaths
Where continent is not null
Group by Location
Order by TotalDeathCount desc


-- Continent wise data on total deaths
Select Location, MAX(cast(total_deaths as int)) AS TotalDeathCount
From PortfolioProject..CovidDeaths
Where continent is null
Group by Location
Order by TotalDeathCount desc


--Vaccination and Deaths table
Select *
From PortfolioProject..CovidDeaths deaths
Join PortfolioProject..CovidVaccinations vac
On deaths.location = vac.location
And deaths.date = vac.date


-- Population and Vaccinations
Select deaths.continent, deaths.location, deaths.date, deaths.population,
vac.new_vaccinations, SUM(cast(vac.new_vaccinations as int)) OVER (Partition by deaths.location Order by deaths.location, deaths.date) AS RollingVaccinations
From PortfolioProject..CovidDeaths deaths
Join PortfolioProject..CovidVaccinations vac
On deaths.location = vac.location
And deaths.date = vac.date
Where deaths.continent is not null
Order by 2,3 



-- Creating a temp table to be able to apply calculations to Alias of rolling people vaccinated 
Drop table if exists #PercentPeopleVaccinated
Create Table #PercentPeopleVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPeopleVaccinated
Select deaths.continent, deaths.location, deaths.date, deaths.population,
vac.new_vaccinations, SUM(cast(vac.new_vaccinations as int)) OVER (Partition by deaths.location Order by deaths.location, deaths.date) AS RollingVaccinations
--(RollingVaccinations/Population)*100
From PortfolioProject..CovidDeaths deaths
Join PortfolioProject..CovidVaccinations vac
On deaths.location = vac.location
And deaths.date = vac.date
Where deaths.continent is not null
--Order by 2,3 

Select *, (RollingPeopleVaccinated/Population)*100
From #PercentPeopleVaccinated


