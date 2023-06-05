--Cleaning Data in SQL

Select *
From PortfolioProject.dbo.NashvilleHousing



--Standardizing Saledate to date format
Select SaleDate, Convert(date, SaleDate)
From PortfolioProject.dbo.NashvilleHousing

Update NashvilleHousing
Set SaleDate = Convert(date, SaleDate)
From PortfolioProject.dbo.NashvilleHousing


--For some reason the Saledate table format didn't update so I am going to add a new column to the Nashvillehouing table and
--update it's values as formatted date
Alter Table NashvilleHousing
Add FormattedSaleDate Date; 

Update NashvilleHousing
Set FormattedSaleDate = Convert(Date, SaleDate)

Select SaleDate, FormattedSaleDate
From NashvilleHousing



--Populating Property Address Data
Select PropertyAddress
From PortfolioProject..NashvilleHousing
--Where PropertyAddress is null

-- Upon inspection of the tables we made an observation that parcelid may repeat but remains unique to the different addresses and
-- at the same time uniqueid is always different. Therefore, if multiple same parcelid's contain any null address then it can be
-- overwritten and replaced with a column which infact does contain the address value. Hence the self join which demonstrates ths observation well.
Select *
From PortfolioProject..NashvilleHousing a
Join PortfolioProject..NashvilleHousing b
    ON a.ParcelID = b.ParcelID
	And a.[UniqueID ] <> b.[UniqueID ]

Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, isnull(a.PropertyAddress, b.PropertyAddress)
From PortfolioProject..NashvilleHousing a
Join PortfolioProject..NashvilleHousing b
    ON a.ParcelID = b.ParcelID
	And a.[UniqueID ] <> b.[UniqueID ]
where a.PropertyAddress is null

Update a
Set a.PropertyAddress = isnull(a.PropertyAddress, b.PropertyAddress)
From PortfolioProject..NashvilleHousing a
Join PortfolioProject..NashvilleHousing b
    ON a.ParcelID = b.ParcelID
	And a.[UniqueID ] <> b.[UniqueID ]



--Breaking address into different elements
Select PropertyAddress
From PortfolioProject..NashvilleHousing

--Charindex(value or element to look for,where to look for) = returns a numerical value
Select 
Substring(PropertyAddress, 1, Charindex(',', PropertyAddress)-1) as SplitAddress
, Substring(PropertyAddress,Charindex(',', PropertyAddress)+1, len(PropertyAddress)) as SplitCity
From PortfolioProject..NashvilleHousing

Alter Table NashvilleHousing
Add SplitAddress nvarchar(255), 
SplitCity nvarchar(255); 

Update NashvilleHousing
Set SplitAddress = Substring(PropertyAddress, 1, Charindex(',', PropertyAddress)-1), 
SplitCity =  Substring(PropertyAddress,Charindex(',', PropertyAddress)+1, len(PropertyAddress)) 

Select *
From NashvilleHousing


--Breaking up owneradress with parsename and replace
--Parsename returns text or element after '.', so the number signifies the element/txt/char encounter number
--parsename reads backwards, hence the numbering 3,2,1

Select
PARSENAME(Replace(OwnerAddress,',','.'), 3),
PARSENAME(Replace(OwnerAddress,',','.'), 2),
PARSENAME(Replace(OwnerAddress,',','.'), 1)
From NashvilleHousing

Alter Table NashvilleHousing
Add SplitOwnerAddress nvarchar(255), 
SplitOwnerCity nvarchar(255),
SplitOwnerState nvarchar(255); 

Update NashvilleHousing
SET SplitOwnerAddress = PARSENAME(Replace(OwnerAddress,',','.'), 3), SplitOwnerCity = PARSENAME(Replace(OwnerAddress,',','.'), 2),
SplitOwnerState = PARSENAME(Replace(OwnerAddress,',','.'), 1)

Select *
From NashvilleHousing


--Changing Y and N to Yes and No in "SoldAsVacant" field
Select distinct(SoldAsVacant), count(SoldAsVacant)
From NashvilleHousing
group by SoldAsVacant
order by 2


Select SoldAsVacant
, Case When SoldAsVacant = 'Y' Then 'Yes'
       When SoldAsVacant = 'N' Then 'No'
	   Else SoldAsVacant
	   End
From NashvilleHousing


Update NashvilleHousing
Set SoldAsVacant = Case When SoldAsVacant = 'Y' Then 'Yes'
       When SoldAsVacant = 'N' Then 'No'
	   Else SoldAsVacant
	   End



--Delete unused column
Select *
From PortfolioProject..NashvilleHousing

Alter table NashvilleHousing
Drop column TaxDistrict