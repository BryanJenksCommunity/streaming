data <- here::here("data","training.csv") %>% 
read_csv() %>% 
as.data.frame()

# data <- data %>% 
  # mutate(exercise = as.factor(data$exercise))
