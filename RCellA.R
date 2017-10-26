RCellA <- function(worldsize = 100, epochs = 100, rule = "184")
{
  dorule <- function(tuple, r = rule)
  {
    if (r == "184")
    {
      rulebook <- c("111" = 1, "110" = 0, "101" = 1,
                    "100" = 1, "011" = 1, "010" = 0,
                    "001" = 0, "000" = 0)
    }
    else
    {
      rulebook <- c("111" = 0, "110" = 1, "101" = 1,
                    "100" = 0, "011" = 1, "010" = 1,
                    "001" = 1, "000" = 0)
    }
    
    return(unname(rulebook[paste(tuple, collapse = "")]))
  }
  
  
  update <- function(row, r = rule)
  {
    
    
    tuples <- matrix(nrow = 3, ncol = length(row))
    tuples[1, ] <- c(0, row[1 : length(row) - 1])
    tuples[2, ] <- row
    tuples[3, ] <- c(row[2 : length(row)], 0)
    
    
    return(apply(tuples, 2, dorule, r = r))
    
  }
  
  world <- matrix(nrow = epochs, ncol = worldsize)
  world[1, ] <- round(runif(worldsize, 0, 1))
  
  for (i in 2 : epochs) {world[i,] <- update(row = world[i - 1,], r = rule)}
  
  return(world)
}
