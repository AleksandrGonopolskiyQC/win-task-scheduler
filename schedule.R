install.packages("taskscheduleR")
library(taskscheduleR)

getCurrentFileLocation <-  function()
{
  this_file <- commandArgs() %>% 
    tibble::enframe(name = NULL) %>%
    tidyr::separate(col=value, into=c("key", "value"), sep="=", fill='right') %>%
    dplyr::filter(key == "--file") %>%
    dplyr::pull(value)
  if (length(this_file)==0)
  {
    this_file <- rstudioapi::getSourceEditorContext()$path
  }
  return(dirname(this_file))
}


script <- normalizePath(file.path(getCurrentFileLocation(), "demo.R"))

## run script once within 30 seconds
taskscheduler_create(taskname = "Demo R Task", rscript = script, schedule = "ONCE", starttime = format(Sys.time() + 30, "%H:%M"))