import logging
from mantis.models.args_model import ArgsModel
from mantis.utils.crud_utils import CrudUtils

class DeboardWorkflow:
    @staticmethod
    async def executor(args: ArgsModel):
        """
        Executes the deboarding process for a given organisation.
        Removes all related organisational data including assets, findings, and extended assets.
        """
        if args.org:
            logging.info(f"Starting deboard process for organisation {args.org}")

            deboard = await CrudUtils.deboard_organisation(args.org)

            if (deboard):
                logging.info(f"Successfully deboarded organisation {args.org}")
                print(f"\n\033[1;32mAll data for {args.org} has been successfully removed from the database\033[0m\n")
        else:
            logging.warning("No organisation specified for deboarding")
